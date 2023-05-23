import requests


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    URL = "https://www.geeksforgeeks.org/data-structures/"
    r = requests.get(URL)
    print(r.content)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
