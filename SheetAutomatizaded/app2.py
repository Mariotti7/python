import openpyxl

# Loading file
book = openpyxl.load_workbook('Sheet Stocks.xlsx')

# Select page
book_statistic = book['Statistics']

# Printing each element line

for rows in book_statistic.iter_rows(min_row=2, max_row=4):
    for cell in rows:
        print(f'{rows[0].value}, {rows[1].value}, {rows[2].value}, {rows[3].value}')