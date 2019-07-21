from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("file:///home/wojtek/PycharmProjects/selenium_udemy/Selenium_files/Test.html")


"""
Sprawdzenie stanu elementu - czy jest enabled.
Np. jeżeli pole tekstowe jest enabled to można wprowadzić wartość, a jak nie to nie.

Pole może być disabled jeżeli dodamy ten atrybut, np. w pliku test.html:
przed: <input type="text" name="fname" id="fname"><br>
po: <input disabled type="text" name="fname" id="fname"><br>
"""

# lokalizuję pole tekstowe:
first_name_input = driver.find_element_by_name("fname")

# sprawdzamy czy element jest dostępny:
if first_name_input.is_enabled():
    # first_name_input.click()
    first_name_input.send_keys("Wojtek")
else:
    print("Element not enabled so you cannot edit it.")
