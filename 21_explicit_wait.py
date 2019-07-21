from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

"""
Metoda explicit wait.
Umozliwia zdefiniowanie warunku, na jaki będziemy czekać i użycie takiego waita w odpowiednim miejscu
w skrypcie

"""

# ponizej klasa z argumentami: browser, timeout, częstotliwosc z jaką bedzie zdefiniowany sprawdzany
# warunek (ponizej co 0.5s oraz to co ma być ignorowane)
wait = WebDriverWait(driver, 10, 0.5) #, NoSuchElementException)

driver.get("file:///home/wojtek/PycharmProjects/selenium_udemy/Selenium_files/Waits2.html")

# lokalizujemy przycisk  i klikamy:
driver.find_element_by_id("clickOnMe").click()

# wywołujemy zmienną wait z metodą until, którą w tym wypadku przyjmuje zaimportowany moduł
# expected_conditions z metodą visibility_... czyli widoczność elementu zlokalizowanego i lokacją
# z argumentami: technika lokalizowania elementu oraz nazwa tagu "p":
wait.until(expected_conditions.visibility_of_element_located((By.TAG_NAME, 'p')))

# wyswietlamy treść paragrafu po tym czasie:
print(driver.find_element_by_tag_name("p").text)
