from datetime import date
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl import Workbook
from openpyxl import load_workbook
from openpyxl.utils.dataframe import dataframe_to_rows
import os.path
import StockData

url_bourse = "https://www.boursorama.com/cours/1rPORA/"
excel_file = "D:/Python_Projects/WebScrapping/stockData.xlsx"


# Function to insert DataFrame below the current date cell
def insert_dataframe(ws, start_row, start_col, df, index_col):
    for r in dataframe_to_rows(df, index=False, header=False):
        ws.append(r)
    if ws["A15"] is not None:
        ws.move_range("A15:D28", rows=-13, cols=4*index_col)
    for cell in ws[start_row][start_col:start_col + len(df.columns)]:
        cell.alignment = Alignment(horizontal='center')


def main():
    today = date.today()

    stock_data = StockData.get_stock_data(url_bourse)
    # stock_data = stock_data.reset_index(drop=True)
    print(type(stock_data))

    if os.path.exists(excel_file):
        wb = load_workbook(excel_file)
        ws = wb.worksheets[0]    # For the moment, unique worksheet existing for debugging purposes.
    else:
        wb = Workbook()
        ws = wb.active
        ws.title = "Orange"

    # Max cols in empty Excel file is 16384. Find the first cell empty and merge and fill it.
    start_col = 2
    index_col = 0
    for i in range(2, 16384, 4):
        cell = ws.cell(1, i)
        index_col = index_col + 1
        if cell.value is None:
            cell.value = today.strftime("%d-%m-%Y")
            ws.merge_cells(None, 1, i, 1, i+3)
            cell.alignment = Alignment(horizontal="center")
            cell.font = Font(bold=True)
            start_col = i
            break
        else:
            print(cell.value)   # Print date of already used cell.
    # Get data in the Excel file.
    insert_dataframe(ws, 2, start_col, stock_data, index_col)

    wb.save(excel_file)

if __name__ == "__main__":
    main()
