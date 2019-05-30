import sys
from urllib.parse import urljoin
import urllib.request
import requests
from bs4 import BeautifulSoup,NavigableString, Tag

def find_link(html):
        soup = BeautifulSoup(html, 'html.parser')
        ignores = ['div.hatnote', 'div.thumb', 'table']

        for ignore in ignores:
            for tag in soup.select(ignore):
                tag.decompose()

        pCount = 0
        for paragraph in soup.find_all(['p', 'ul', 'ol']):
            for child in paragraph.children:
                if child.__class__ == NavigableString:
                    if '(' in child.string:
                        pCount += child.string.count('(')
                    if ')' in child.string:
                        pCount -= child.string.count(')')
                    if pCount < 0:
                        pCount = 0
                    continue

                def match_found(x):
                    return x.name == 'a' and pCount == 0

                if child.__class__ == Tag and match_found(child):
                    href = child['href'] if child['href'].startswith('http') \
                        else 'http:{}'.format(child['href'])
                    return (href.replace('&action=render', '')
                        .replace('?action=render', '')
                        .replace('http://en.wikipedia.org/wiki/', '')
                        .replace('https://en.wikipedia.org/wiki/', '')
                        .replace('https://en.wikipedia.org/w/index.php?title=', ''))

def navigate_to_philosophy(start_url):
    link_list = []

    try:
        response = requests.get(start_url, params={'action': 'render'}, timeout=5)
    except requests.exceptions.RequestException:
        return None

    init_link = find_link(response.text)
    if not init_link:
        return None
    link_list.append("https://en.wikipedia.org/wiki/" + init_link)
    print(link_list[0])

    i = 0
    while True:
        if "philosophy" == link_list[i].rpartition('/')[2].lower():
            break

        try:
            curr_response = requests.get(link_list[i], params={'action': 'render'}, timeout=.5)
        except requests.exceptions.RequestException:
            return None 

        curr_link = find_link(curr_response.text)
        if not curr_link or "redlink" in curr_link:
            return None
        new_link = "https://en.wikipedia.org/wiki/" + curr_link
        for i in range(len(link_list)):
            if new_link in link_list[i] :
                return None
        link_list.append(new_link)
        print(new_link)
        i += 1
    return link_list

if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/Accenture"
    print(url)
    navigate_to_philosophy(url)