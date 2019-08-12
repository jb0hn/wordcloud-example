# IMPORT MODULES

import os
import wikipedia as w # gets wikipedia page
from wordcloud import WordCloud as wc # creates word cloud
from wordcloud import STOPWORDS as sw # removes chosen words from cloud
from PIL import Image as image # to import image into python
import numpy as np # to convert image to array

# SET UP
currdir = os.path.dirname(__file__) # keeps track of current directory to avoid errors


# CLASSES
class w_Cloud(object):
    def __init__(self, name, query):
        self.name = name
        self.query = query

    def __str__(self):
        return self.name

    # METHODS
    # create function which search for result in the wikipedia and returns the content of the first matched to the query; eg. get_wiki('python') -> returns content of the subpage about python programming language
    def get_wiki(self):
        title = w.search(self.query)[0] # get first result
        page = w.page(title) # get page

        return page.content # return page content


    # main method
    def create(self):
        text = self.get_wiki()
        name = self.name

        mask = np.array(image.open(os.path.join(currdir, 'cloud.png'))) # mapping the image into array
        stop_words = set(sw) # create a set of words to avoid in word cloud

        cloud = wc(
        background_color='white', # color of backgroud
        mask=mask,  # mask
        max_words=200, # number of words in cloud
        stopwords=stop_words # words to avoid in cloud
        )

        print("Working...")

        cloud.generate(text) # creates the word cloud

        cloud.to_file(os.path.join(currdir, '{}.png'.format(name))) # saves the word cloud as a file

# MAIN
def main():
        os.system('cls' if os.name == 'nt' else 'clear') # clear screen

        name = input("How do you want to name your cloud: ")
        query = input("What topic on Wikipedia are you looking for: ")

        word_cloud = w_Cloud(name, query)
        word_cloud.create()
        print("Success.")


# RUN
main()
