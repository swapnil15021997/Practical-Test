import urllib.request #imported url library.

#variable url is taking input from user
class ReadFile:
    def __init__(self):
        url = input("Enter the url here")
        #urlopen function opens file associated with the url
        file = urllib.request.urlopen(url)

        #for loop is to print each line 

        for line in file:
            lines = line.decode("utf-8")
            print(lines)
ReadFile()
