from datetime import date
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl import Workbook
from openpyxl import load_workbook
from openpyxl.utils.dataframe import dataframe_to_rows
import os.path
import StockData

url_bourse = "https://www.boursorama.com/cours/"
excel_file = "D:/Python_Projects/WebScrapping/stockData.xlsx"
stocks_dict = {
    'Orange' : "1rPORA/",
    'Alstom' : "1rPALO/"
}


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

    if os.path.exists(excel_file):
        wb = load_workbook(excel_file)
        ws = wb.worksheets[0]  # For the moment, unique worksheet existing for debugging purposes.
    else:
        wb = Workbook()
        for key in stocks_dict.keys():
            wb.create_sheet(key)   # Create a worksheet per company.
        del wb['Sheet']     # Remove worksheet created by default.
        wb.save(excel_file)

    for key in stocks_dict.keys():
        # stocks_dict['key']
        url_data = url_bourse + stocks_dict[key]
        print(url_data)
        stock_data = StockData.get_stock_data(url_data)
        print(type(stock_data))
        print(stock_data)

        for ws in wb.worksheets:
            if ws.title != key: continue
            else:
                # Max cols in empty Excel file is 16384. Find the first cell empty and merge and fill it.
                index_col = 0  # Used as index to shift data after first day recovering data.
                for i in range(1, 16384, 4):
                    cell = ws.cell(1, i)
                    if cell.value is None:
                        cell.value = today.strftime("%d-%m-%Y")
                        ws.merge_cells(None, 1, i, 1, i + 3)
                        cell.alignment = Alignment(horizontal="center")
                        cell.font = Font(bold=True)
                        index_col = index_col + 1
                        break
                    else:
                        print(cell.value)  # Print date of already used cell.
                    # Get data in the Excel file.
                insert_dataframe(ws, 2, 1, stock_data, index_col)
                wb.save(excel_file)


if __name__ == "__main__":
    main()
