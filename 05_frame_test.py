from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("file:///home/wojtek/PycharmProjects/selenium_udemy/Selenium_files/iFrameTest.html")
driver.maximize_window()

"""
Obsługa iframe.
iframe - specjalny tag HTML, który umożliwia umieszczenie strony wewnątrz takiego tagu
czyli taka strona w stronie. Żeby wyświetlić to co jest na takiej wbudowanej stronie,
należy użyć iframe'a właśnie.
"""

# spr. jaką wartość tekstową ma nagłówek h1:
print(driver.find_element_by_tag_name("h1").text)

# przełączamy się do iframe'a i wyświetlamy jego zawartość czyli stronę www:
driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
print(driver.find_element_by_tag_name("h1").text)

# przełączamy się z powrotem do pierwotnego iframe'a (nadrzędna strona):
driver.switch_to.default_content()
print(driver.find_element_by_tag_name("h1").text)
