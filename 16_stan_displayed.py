from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("file:///home/wojtek/PycharmProjects/selenium_udemy/Selenium_files/Test.html")

"""
Spr. czy element jest wyświetlony na stronie (is_displayed).

Czy istnieje na stronie i się wyświetla userowi czy jest, ale nie wyswietla się.

W kodzie test.html jest paragraf typu hidden - to jest sprawdzamy
"""


# lokalizuję paragraf:
paragraph = driver.find_element_by_tag_name("p")

# sprawdzamy czy element jest wyswietlony. Jeżeli tak to pobieramy tekst z niego,
# a jezeli nie jest wyswietlony to pobieramy zawartosc ukrytego elementu:

if paragraph.is_displayed():
    print("Element is displayed")
    print(paragraph.text)
else:
    print("Element is not displayed")
    print(paragraph.get_attribute("textContent"))
