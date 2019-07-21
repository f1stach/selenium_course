from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("file:///home/wojtek/PycharmProjects/selenium_udemy/Selenium_files/Test.html")
driver.maximize_window()

"""
Klikanie na element i ustawianie wartości pola tekstowego przy pomocy JavaScript.
Stosować tam gdzie metody send_keys i click nie działają.
"""

# przyznajemy dostęp do metody execute_script z kodem JS i klikamy nim na przycisk:
driver.execute_script("arguments[0].click();", driver.find_element_by_id("newPage"))

# ustawiamy wartość atrybutu value kodem JS:
wartosc = "Wojtek"
driver.execute_script("arguments[0].setAttribute('value', '" + wartosc + "')", driver.find_element_by_id("fname"))
