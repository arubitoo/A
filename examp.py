from urllib.request import urlopen
import urllib.request

def read_file():
    contents = open(r"C:\\Users\\HP\\Desktop\\curisewords\\movie_codes.txt")
    quotes = contents.read()
    check_badwords(quotes)


def check_badwords(word_tocheck):
        connection = urllib.request.urlopen("http: // www.wdylike.appspot.com /?q=sit")
        output = connection.read()
        print(output)


'''read_file()'''