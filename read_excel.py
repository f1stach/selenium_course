"""
Plik zawierający kod umożliwiający przeczytanie danych z Excela.
"""

import xlrd


wb = xlrd.open_workbook("Selenium_files/Dane.xlsx")

# pobierz arkusz po indexie (od zera)
sheet = wb.sheet_by_index(0)

# dla wszystkich elementów od 1 do liczby wierszy (bez 0, bo tam są nagłówki)
# i dla wszystkich elementów w zakresie liczby kolumn
for i in range(1, sheet.nrows):
    for j in range(sheet.ncols):
        print(sheet.cell(i, j).value)
