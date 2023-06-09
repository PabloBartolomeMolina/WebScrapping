import requests
import csvLocal
import graphGeneration
from bs4 import BeautifulSoup


csvFile = 'champions.csv'


def webScrapping_Table(web_url):
    champsDict = {"Year": "Driver"}

    r = requests.get(web_url)   # Get content from web page.
    # print(r.content)

    soup = BeautifulSoup(r.content, 'html.parser')  # Parse the HTML of the web page.
    # results = soup.find(id="racingnews365_ros_alpha_leaderboard-billboard") # get full web content

    # Get the contents of the specific table that contains the desired content : List of World Champions by year.
    # Parameters will vary depending on the content we want to retrieve.
    results = soup.find("table",
                        {"class": "table-default table-default--expanded content-field__table"})  # get table contents
    # print(results.prettify())  # Print the content of extracted data.

    rows = results.find_all("tr")  # Look for rows in the table with proper header identifier.
    for row in rows:
        cells = row.findAll("td")  # Look for each cell using proper identifier.
        if len(cells) == 2:
            year = cells[0].find(text=True).replace(" ", "")    # Make it more readable when printing out.
            year = year.replace("\n\t\t\t\t\t\t", "")    # Make it more readable when printing out.
            year = year.replace("\n", "")    # Make it more readable when printing out.
            name = cells[1].find(text=True).replace(" ", "")    # Mate it more readable when printing out.
            name = name.replace("\n\t\t\t\t\t\t", "")    # Mate it more readable when printing out.
            name = name.replace("\n", "")    # Mate it more readable when printing out.
            champsDict[year] = name
    print (champsDict)
    csvLocal.csvTable(champsDict, csvFile)
    graphGeneration.generate_graph(csvFile)
