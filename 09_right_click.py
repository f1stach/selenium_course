from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("file:///home/wojtek/PycharmProjects/selenium_udemy/Selenium_files/DoubleClick.html")
driver.maximize_window()

"""
Symulowanie kliknięcia prawym przyciskiem myszy.

Korzystamy z funkcji z klasy ActionChains. Na stronie testowej powinno pokazać się
menu kontekstowe
"""

# odnajdujemy przycisk na stronie:
button = driver.find_element_by_id("bottom")

# korzystamy z klasy ActionChains do wywołania prawokliku:
webdriver.ActionChains(driver).context_click(button).perform()
