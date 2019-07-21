from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

"""
Metoda Implicit wait
Poczeka na element do czasu aż pojawi się na stronie.

używamy funkcji implicitly_wait i podajemy liczbe sekund jaką ma czekać na 
pojawienie się treści. Minusem jest to, że podpina się do każdego elementu w skrypcie.
"""

driver.implicitly_wait(10)

driver.get("file:///home/wojtek/PycharmProjects/selenium_udemy/Selenium_files/Waits2.html")

# lokalizujemy przycisk  i klikamy:
driver.find_element_by_id("clickOnMe").click()

# test dot. lokalizacji nieistniejącego elementu:
# funkcja będzie dobijać się przez 10 sekund do elementu, ale go nie znajdzie i
# zwróci error NoSuchElementException
driver.find_element_by_id("clickOnMe11").click()

# wyswietlamy treść paragrafu po tym czasie:
print(driver.find_element_by_tag_name("p").text)
