from datetime import date
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter
from openpyxl import Workbook
from openpyxl import load_workbook
from openpyxl.utils.dataframe import dataframe_to_rows
import os.path
import StockData

url_bourse = "https://www.boursorama.com/cours/1rPORA/"
excel_file = "D:/Python_Projects/WebScrapping/stockData.xlsx"

# Function to insert DataFrame below the current date cell
def insert_dataframe(ws, start_row, start_col, df):
    for r in dataframe_to_rows(df, index=False, header=False):
        ws.append(r)
    for cell in ws[start_row][start_col:start_col + len(df.columns)]:
        cell.alignment = Alignment(horizontal='center')


def main():
    today = date.today()

    stock_data = StockData.get_stock_data(url_bourse)
    # stock_data = stock_data.reset_index(drop=True)
    print(type(stock_data))

    if os.path.exists(excel_file):
        wb = load_workbook(excel_file)
        ws = wb.worksheets['Orange'] # For the moment, unique worksheet existing for debugging purposes.
    else:
        wb = Workbook()
        ws = wb.active
        ws.title = "Orange"
        ws['A1'] = "DATE :"
        ws['A1'].font = Font(bold=True)

    # Max cols in empty Excel file is 16384. Find the first cell empty and merge and fill it.
    for i in range(2, 16384, 4):
        cell = ws.cell(1, i)
        if cell.value is None:
            cell.value = today.strftime("%d-%m-%Y")
            ws.merge_cells(None, 1, i, 1, i+3)
            cell.alignment = Alignment(horizontal="center")
            cell.font = Font(bold=True)
            break
        else:
            print("ERROR")
    # Get data in the Excel file.
    for r in dataframe_to_rows(stock_data, index=True, header=True):
        ws.append(r)

    wb.save(excel_file)


if __name__ == "__main__":
    main()
