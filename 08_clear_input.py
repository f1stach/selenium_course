from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("file:///home/wojtek/PycharmProjects/selenium_udemy/Selenium_files/Test.html")
driver.maximize_window()

"""
Usuwanie danych z pola tekstowego.
W inpucie nie raz są już wpisane dane, więc trzeba to wyczyścić, żeby testować.

Funkcja clear.

Uzycie funkcji find_by_name("username").send_keys("abcd") bez clear sprawi, że tekst 
zostanie dopisany do tego co jest juz w polu tekstowym input
"""

username_input = driver.find_element_by_name("username")
username_input.clear()
username_input.send_keys("PonuryZniwiarz")
