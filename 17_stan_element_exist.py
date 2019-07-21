from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("file:///home/wojtek/PycharmProjects/selenium_udemy/Selenium_files/Test.html")

"""
Spr. czy element istnieje na stronie.

Brak wbudowanej funkcji, ale sa dwie metody:
- find_elements_by... - zwraca listę elementów. Jeżeli nie uda się znaleźć elementu na stronie
to długość listy = 0
- blok try except poprzez dodanie wyjątku
"""

# lokalizuję element nieistniejący na stronie - jest błąd NoSuchElementException:
# elements = driver.find_element_by_tag_name("papa")


# Metoda nr 1:

# lokalizuję element nieisntniejący na stronie - brak błędu dla elements:
elements = driver.find_elements_by_tag_name("input")

if len(elements) > 0:
    print("Element istnieje na stronie")
else:
    print("Brak elementu na stronie")


# Metoda nr 2:

try:
    driver.find_element_by_tag_name("p")
    print("Element istnieje na stronie")
except NoSuchElementException:
    print("Element nie istnieje")
