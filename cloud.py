import os

from os import path
from wordcloud import WordCloud

file = input("What file of text do you want to make a wordcloud?\n")
outfile = file.replace(".txt", ".png")

with open(file) as this_file:
    text = this_file.read()

wordcloud = WordCloud(width = 1600, height = 1200,
                      random_state=1,
                      colormap='Reds',
                      collocations = False,
                      regexp = r"\w[\w' ]+").generate(text)
wordcloud.to_file(outfile)