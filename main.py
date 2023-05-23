import requests
from bs4 import BeautifulSoup

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    URL = "https://www.geeksforgeeks.org/data-structures/"
    r = requests.get(URL)
    print(r.content)
    print("\n\n\n")

    soup = BeautifulSoup(r.content, 'html5lib')
    print(soup.prettify())
