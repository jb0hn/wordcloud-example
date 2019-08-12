# wordcloud-wikipedia
Simple program to create word clouds from Wikipedia articles.

## What is a word cloud?
An image composed of words used in a particular text or subject, in which the size of each word indicates its frequency or importance.

## Quick run in the browser
1. Cick in the link:
https://repl.it/@jb0hn/wordcloud-wikipedia

2. After being redirected to the Repl.it website, make sure that "main.py" file is open and then click green button "Run" in the top bar of the page.


## Installation

Install [wordcloud](https://github.com/amueller/word_cloud) using a simple pip command.

```
pip install wordcloud
```

**wikipedia** library is used for extracting Wikipedia articles on any given topic. Install it using this pip command:
```
pip install wikipedia
```
## Usage

Run python script as:

```
python word_cloud.py
```

For example:

```
python word_cloud.py

How do you want to name your cloud: python
What topic on Wikipedia are you looking for: python
```

will create word cloud for the topic 'python' which looks like this:

![](https://raw.githubusercontent.com/jb0hn/wordcloud-example/master/python.png)
