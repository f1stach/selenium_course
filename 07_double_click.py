from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("file:///home/wojtek/PycharmProjects/selenium_udemy/Selenium_files/DoubleClick.html")
driver.maximize_window()

"""
Symulowanie podwójnego kliknięcia myszki
"""

# odnajdujemy przycisk na stronie:
button = driver.find_element_by_id("bottom")

# wywołanie kliknięcia x2 - tak jak poniżej nie zadziała jako symulacja dwukliku:
# button.click()
# button.click()

# wywołanie dwukliku specjalną klasą ActionChains - argument to nasza przeglądarka
# metoda double_click z parametrem jako nasz przycisk
# metoda perform aby akcja zostałą wywołana
webdriver.ActionChains(driver).double_click(button).perform()
