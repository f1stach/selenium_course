from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("file:///home/wojtek/PycharmProjects/selenium_udemy/Selenium_files/Waits2.html")

"""
Metoda Sleep.
Jedna z metod, które czekają na okreslone warunki, np. z powodu słabego połączenia int.

Korzystamy z Waits2.html, w którym nie ma hidden paragraph, ale trzeba kliknąć
przycisk, żeby pojawił się tekst.
"""

# lokalizujemy przycisk  i klikamy:
driver.find_element_by_id("clickOnMe").click()

# podajemy czas jaki chcemy poczekac czyli skrypt jest zatrzymywany na ten czas
time.sleep(5)

# wyswietlamy treść paragrafu po tym czasie czyli w momencie gdy paragraf przestał być hidden:
print(driver.find_element_by_tag_name("p").text)

"""
Metoda sleep nie jest wydajna. Może sprawić, że test będzie wykonywał się wolno,
ale ciężko trafić z czasem, bo mogą pojawić się problemy z siecią. Podejście
nieelastyczne, nie jest rekomendowane.
"""
