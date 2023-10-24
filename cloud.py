from wordcloud import WordCloud

filename = input("What file of text do you want to make a wordcloud?\n")
outfile = filename.replace(".txt", ".png")

with open(filename) as this_file:
    text = this_file.read()

wordcloud = WordCloud(width = 1600, height = 1200,
                      random_state=1,
                      colormap='Reds',
                      collocations = False,
                      regexp = r"\w[\w' ]+").generate(text)
wordcloud.to_file(outfile)