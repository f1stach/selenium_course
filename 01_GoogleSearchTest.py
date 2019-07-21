from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

"""
Poniżej sytuacja gdy nie mamy managera driverów - należy pobrać driver na dysk i importować.
"""

# # tworzymy nową przeglądarkę Chrome za pomocą testu:
# driver = webdriver.Chrome("/home/wojtek/PycharmProjects/selenium_udemy/drivers/chromedriver")
#
# # pobieramy konkretną stronę, która zostanie otwarta w przeglądarce przez test:
# driver.get("http://www.google.com")


"""
Poniżej sytuacja gdy mamy zainstalowany webdriver-manager - argument dla Chrome to nasz driver bez pobierania na dysk.
"""

# tworzymy nową przeglądarkę Chrome za pomocą testu:
driver = webdriver.Chrome(ChromeDriverManager().install())

# pobieramy konkretną stronę, która zostanie otwarta w przeglądarce przez test:
driver.get("http://www.google.com")

# ustawiamy wielkość okna przeglądarki na sztywno po odpaleniu przez test:
# driver.set_window_size(1600, 1200)

# maksymalizacja okna przeglądarki za pomocą jednej funkcji bez sztywnych wartości:
driver.maximize_window()