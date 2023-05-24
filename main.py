import requests
from bs4 import BeautifulSoup

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    URL = "https://racingnews365.com/every-world-champion-in-formula-1-history"
    r = requests.get(URL)
    # print(r.content)

    soup = BeautifulSoup(r.content, 'html.parser')
    # results = soup.find(id="racingnews365_ros_alpha_leaderboard-billboard") # get full web content
    results = soup.find("table",
                        {"class": "table-default table-default--expanded content-field__table"})  # get table contents
    # print(results.prettify())  # print the content of extracted data

    rows = results.find_all("tr")  # look for rows in the table with proper header identifier
    # print("Champions:")
    # print(champions)
    for row in rows:
        cells = row.findAll("td")  # look for each cell using proper identifier
        if len(cells) == 2:
            year = cells[0].find(text=True).replace(" ", "")
            name = cells[1].find(text=True).replace(" ", "")
            printable = year + " : " + name
            print(year.replace("\n", "") + name.replace("\n", "") + "\n")
