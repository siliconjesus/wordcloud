import os

from os import path
from wordcloud import WordCloud

d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()
file = input("What file of text do you want to make a wordcloud? ")
outfile = file.replace(".txt", ".png")

text = open(path.join(d, file)).read()

wordcloud = WordCloud(random_state=1,
                      colormap='Reds',
                      collocations = False,
                      regexp = r"\w[\w' ]+").generate(text)
wordcloud.to_file(outfile)