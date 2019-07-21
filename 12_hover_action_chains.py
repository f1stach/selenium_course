from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.w3schools.com")

"""
Łańcuchy akcji.
Jak łączyć akcje z klasy ActionChains, np. przesunięcie elementu i kliknięcie na niego
"""


# lokalizujemy element na stronie:
tutorials_element = driver.find_element_by_id("navbtn_tutorials")

# najezdzamy na element aby podswietlil sie na bialo i został kliknięty (pokaże sie menu):
webdriver.ActionChains(driver).move_to_element(tutorials_element).click(tutorials_element).perform()
