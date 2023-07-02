from datetime import date
from openpyxl.styles import Alignment
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows
import StockData

url_bourse = "https://www.boursorama.com/cours/1rPORA/"


def main():
    today = date.today()

    stock_data = StockData.get_stock_data(url_bourse)
    # stock_data = stock_data.reset_index(drop=True)
    print(type(stock_data))

    wb = Workbook()
    ws = wb.active
    ws['A1'] = "DATE :"
    ws.merge_cells(None, 1, 2, 1, 5)
    ws['B1'] = today.strftime("%d-%m-%Y")
    ws['B1'].alignment = Alignment(horizontal="center")
    for r in dataframe_to_rows(stock_data, index=True, header=True):
        ws.append(r)
    try:
        wb.save("stockData.xlsx")
    except:
        print("An exception occurred")


if __name__ == "__main__":
    main()
