from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("file:///home/wojtek/PycharmProjects/selenium_udemy/Selenium_files/Test.html")

"""
Spr. czy element typu checkbox jest wybrany/zaznaczony.
Chcemy też kontrolować jego stan.
"""

# lokalizuję checkboxa:
checkbox = driver.find_element_by_xpath("//input[@type='checkbox']")

# sprawdzamy stan elementu gdy kliknięty lub nie:

# checkbox.click()

if checkbox.is_selected():
    print("Wartość zaznaczona! Odznaczam!")
    checkbox.click()
else:
    print("Niezaznaczony więc zaznaczam wartosc")
    checkbox.click()
