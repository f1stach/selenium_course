import os

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("file:///home/wojtek/PycharmProjects/selenium_udemy/Selenium_files/FileUpload.html")

"""
Tworzenie screenshota - zrzutu okna przeglądarki. C.d. upload plików.

Mozna to wykorzystać w celu raportowym albo badania poprawności testów czy debuggowaia.

Najpierw tworzymy folder screenshots, w którym będa zrzuty.
"""

upload_input = driver.find_element_by_id("myFile")

# wprowadzamy sciezke pliku do uploadu:
path = os.path.abspath("Selenium_files/uploadMe.txt")

# robimy screenshota przed wgraniem:
driver.save_screenshot("screenshots/before_upload.png")

# wysylamy scieżke do inputa za pomocą send_keys; obok przycisku widac nazwę pliku
upload_input.send_keys(path)

# tworzenie zrzutu ekranu przeglądarki po uploadzie:
driver.save_screenshot("screenshots/after_upload.png")
