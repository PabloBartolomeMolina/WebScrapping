import requests
from bs4 import BeautifulSoup
import csv

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    URL = "https://racingnews365.com/every-world-champion-in-formula-1-history"
    r = requests.get(URL)
    #print(r.content)

    soup = BeautifulSoup(r.content, 'html.parser')
    results = soup.find(id="racingnews365_ros_alpha_leaderboard-billboard")
    #print(results)
    print(results.prettify())
