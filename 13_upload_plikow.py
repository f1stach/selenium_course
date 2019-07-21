import os

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("file:///home/wojtek/PycharmProjects/selenium_udemy/Selenium_files/FileUpload.html")

"""
Upload plików na stronie.

Przycisk do uploadu to zwykły input, ale typu file.
"""

upload_input = driver.find_element_by_id("myFile")

# wprowadzamy sciezke pliku do uploadu:
path = os.path.abspath("Selenium_files/uploadMe.txt")

# wysylamy scieżke do inputa za pomocą send_keys; obok przycisku widac nazwę pliku
upload_input.send_keys(path)
