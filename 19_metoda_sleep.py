from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("file:///home/wojtek/PycharmProjects/selenium_udemy/Selenium_files/Waits.html")

"""
Metoda Sleep.
Jedna z metod, które czekają na okreslone warunki, np. z powodu słabego połączenia int.

Korzystamy z Waits.html, które ma ukryty paragraf, który pojawi się po określonym czasie
od naciśnięcia przycisku na stronie.
"""

# lokalizujemy przycisk  i klikamy:
driver.find_element_by_id("clickOnMe").click()

# podajemy czas jaki chcemy poczekac czyli skrypt jest zatrzymywany na ten czas
time.sleep(5)

# wyswietlamy treść paragrafu po tym czasie czyli w momencie gdy paragraf przestał być hidden:
print(driver.find_element_by_tag_name("p").text)

