#Alert us when the site is working or not
#Import urllib
import urllib
import urllib.request as uro

def main(url):
    try:
        response = uro.urlopen(url)
        print(response.getcode())
    except ValueError:
        print('Incorrect url')

input_url = input('Enter url: ')
main(input_url)