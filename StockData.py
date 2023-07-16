import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
import matplotlib.pyplot as plt


def get_stock_data(stock_url):
    response = requests.get(stock_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    dfs = pd.read_html(response.text)  # List with content of the table of data we look for.
    print(type(dfs))

    dfRet = dfs[0]

    dfFound = 0
    for df in dfs:
        # iterating the columns
        for col in df.columns:
            if col != 'période':
                dfFound = 0
            else:
                dfFound = 1
                dfRet = df
                break
        if dfFound != 1:
            print('Keep looking')
        else:
            break
    return dfRet


def save_data_to_csv(stock_data, filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Timeframe', 'Stock Value'])

        for timeframe, value in stock_data.items():
            writer.writerow([timeframe, value])


def plot_graph(stock_data):
    timeframes = list(stock_data.keys())
    values = list(stock_data.values())

    plt.figure(figsize=(8, 6))
    plt.bar(timeframes, values)
    plt.xlabel('Timeframe')
    plt.ylabel('Stock Value')
    plt.title('Stock Evolution')
    plt.show()
