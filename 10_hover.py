from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.w3schools.com")

"""
Najechanie na element - hover.

Najazd na element powoduje dodatkowe opcje lub dochodzi do zmiany stanu, np. zmiana
koloru.
"""

# lokalizujemy element na stronie:
tutorials_element = driver.find_element_by_id("navbtn_tutorials")

# najezdzamy na element aby podswietlil sie na bialo:
webdriver.ActionChains(driver).move_to_element(tutorials_element).perform()
