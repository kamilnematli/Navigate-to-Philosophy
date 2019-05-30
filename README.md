# Navigate to Philosophy

TASK

Please write a Python script to check the “Getting to Philosophy” law.
https://en.wikipedia.org/wiki/Wikipedia:Getting_to_Philosophy

Clicking on the first link in the main body of a Wikipedia article and repeating the process for subsequent articles would usually lead to the article Philosophy.

The program should receive a Wikipedia link as an input, go to another normal link and repeat this process until either Philosophy page is reached, or we are in an article without any outgoing wikilinks, or stuck in a loop.

A “normal link” is a link from the main page article, not in a box, is blue (red is for non-existing articles), not in parentheses, not italic and not a footnote. You don’t have to check style tables or other fancy things, it is enough that the script works with current wikipedia style (for example you can use ‘class’ attribute in Wikipedia tags). For easy validation, please print all visited links to the standard output.

Use a 0.5 second timeout between queries to avoid heavy load on Wikipedia.

You can use https://en.wikipedia.org/wiki/Special:Random for testing.
