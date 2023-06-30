import StockData
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows

url_bourse = "https://www.boursorama.com/cours/1rPORA/"

def main():
    stock_data = StockData.get_stock_data(url_bourse)
    print(type(stock_data))
    wb = Workbook()
    ws = wb.active
    for r in dataframe_to_rows(stock_data, index=True, header=True):
        ws.append(r)
    wb.save("stockData.xlsx")

if __name__ == "__main__":
    main()
