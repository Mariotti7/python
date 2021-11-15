import openpyxl

book= openpyxl.Workbook()

book.create_sheet('computadores')

book_page=book['computadores']

book_page.append(['Eletrônica, memória ram, preço'])
book_page.append(['Computador 1, 8gb  ram, R$2500'])
book_page.append(['Computador 2, 16gb ram, R$5500'])
book_page.append(['Computador 3, 32gb ram, R$8500'])

book.save('meus computadores.xlsx')



