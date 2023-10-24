import sys
from wordcloud import WordCloud

# opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
# args = [arg for arg in sys.argv[1:] if not arg.startswith("-")]

# def print_help():
#     print(sys.argv[0] + " [-h][-v][-V][--help][--version][--verbose]")
#     exit()

# def print_version():
#     print(sys.argv[0] + " version 0.1")
#     exit()

# def verbose_on():
#     print(sys.argv[0] + " Verbose on")

# if "-h" in opts:
#     print_help()
# if "--help" in opts:
#     print_help()
# if "-v" in opts:
#     print_version()
# if "--version" in opts:
#     print_version()
# if "-V" in opts:
#     verbose_on()
# if "--verbose" in opts:
#     verbose_on()

filename = input("What file of text do you want to make a wordcloud?/n")
outfile = filename.replace(".txt", ".png")

with open(filename) as this_file:
    text = this_file.read()

wordcloud = WordCloud(width = 1600, height = 1200,
                      random_state=1,
                      colormap='Reds',
                      collocations = False,
                      regexp = r"\w[\w' ]+").generate(text)
wordcloud.to_file(outfile)