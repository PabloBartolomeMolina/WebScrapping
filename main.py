from datetime import date
from openpyxl.styles import Alignment, Font
from openpyxl import Workbook
from openpyxl import load_workbook
from openpyxl.utils.dataframe import dataframe_to_rows
import os.path
import StockData
import graphGeneration

url_bourse = "https://www.boursorama.com/cours/"
excel_file = "D:/Python_Projects/WebScrapping/stockData.xlsx"
stocks_dict = {
    'Orange': "1rPORA/",
    'Alstom': "1rPALO/"
}
stockList = []
currentVarList = []
weekVarList = []
monthVarList = []
month3VarList = []
month6VarList = []
yearVarList = []
year3VarList = []
year5VarList = []
year10VarList = []


# Function to insert DataFrame below the current date cell
def insert_dataframe(ws, start_row, start_col, df, index_col):
    for r in dataframe_to_rows(df, index=False, header=False):
        ws.append(r)
    if ws["A15"] is not None:
        ws.move_range("A15:D28", rows=-13, cols=4 * index_col)
    for cell in ws[start_row][start_col:start_col + len(df.columns)]:
        cell.alignment = Alignment(horizontal='center')


def main():
    if os.path.exists(excel_file):
        wb = load_workbook(excel_file)
        companies_list = list(stocks_dict.keys())
        companies_list.sort()
        for key in companies_list:
            if key in wb.sheetnames:
                print(key, " already present")
                continue
            else:
                print(key, " newly added")
                wb.create_sheet(key)  # Create a worksheet for newly added company.
    else:
        wb = Workbook()
        for key in stocks_dict.keys():
            wb.create_sheet(key)  # Create a worksheet per company.
        del wb['Sheet']  # Remove worksheet created by default.
        wb.save(excel_file)

    for key in stocks_dict.keys():
        url_data = url_bourse + stocks_dict[key]
        stock_data = StockData.get_stock_data(url_data)
        stockList.append(key)
        currentVarList = stock_data.values[0][1]
        weekVarList = stock_data.values[1][1]
        monthVarList = stock_data.values[2][1]
        month3VarList = stock_data.values[3][1]
        month6VarList = stock_data.values[4][1]
        yearVarList = stock_data.values[5][1]
        year3VarList = stock_data.values[6][1]
        year5VarList = stock_data.values[7][1]
        year10VarList = stock_data.values[8][1]

        for ws in wb.worksheets:
            if ws.title != key:
                continue
            else:
                # Max cols in empty Excel file is 16384. Find the first cell empty and merge and fill it.
                index_col = 0  # Used as index to shift data after first day recovering data.
                for i in range(1, 16384, 4):
                    cell = ws.cell(1, i)
                    if cell.value is None:
                        cell.value = date.today().strftime("%d-%m-%Y")
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

        graphGeneration.plot_yearVariation(stockList, currentVarList, weekVarList, monthVarList, month3VarList,
                                           month6VarList, yearVarList, year3VarList, year5VarList, year10VarList)


if __name__ == "__main__":
    main()
