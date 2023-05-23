import requests
from bs4 import BeautifulSoup
import csv

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    URL = "https://racingnews365.com/every-world-champion-in-formula-1-history"
    r = requests.get(URL)
    print(r.content)

    soup = BeautifulSoup(r.content, 'html5lib')

    data = []
    table = soup.find('div', attrs={'class': 'panel__content'})
    table_body = table.findAll('div', attrs={'class': 'qti-listm'})

    #rows = table_body.find_all('tr')
    for row in table_body:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])  # Get rid of empty values

    filename = 'inspirational_quotes.csv'
    with open(filename, 'w', newline='') as f:
        w = csv.DictWriter(f, ['Year', 'Driver'])
        w.writeheader()
        for quote in data:
            w.writerow(data)
'''
    table = soup.find("table", { "class" : "lineItemsTable" })
    for row in table.findAll("tr"):
        cells = row.findAll("td")
        if len(cells) == 9:
            summons = cells[1].find(text=True)
            plateType = cells[2].find(text=True)
            vDate = cells[3].find(text=True)
            location = cells[4].find(text=True)
            borough = cells[5].find(text=True)
            vCode = cells[6].find(text=True)
            amount = cells[7].find(text=True)
            print amount
'''