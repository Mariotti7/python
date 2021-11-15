import openpyxl

book = openpyxl.load_workbook('meus computadores.xlsx')

book_page = book['computadores']

for rows in book_page.iter_rows(min_row=2, max_row=4):
    for cell in rows:
        print(f'{rows[0].value}, {rows[1].value}, {rows[2].value}, {rows[3].value}')