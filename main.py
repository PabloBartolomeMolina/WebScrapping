from datetime import date
from openpyxl.styles import Alignment
from openpyxl.styles import Font
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
    ws.title = "Orange"
    ws['A1'] = "DATE :"
    # Merge cells to set date for a given set of data.
    ws.merge_cells(None, 1, 2, 1, 5)
    ws['B1'] = today.strftime("%d-%m-%Y")
    ws['B1'].alignment = Alignment(horizontal="center")
    # Get data in the Excel file.
    for r in dataframe_to_rows(stock_data, index=True, header=True):
        ws.append(r)
    # First row in bold.
    for row in ws.iter_rows(min_row=ws.min_row, max_row=ws.min_row, min_col=1, max_col=ws.max_column):
        for cell in row:
            cell.font = Font(bold=True)
    wb.save("stockData.xlsx")


if __name__ == "__main__":
    main()
