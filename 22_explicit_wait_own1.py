from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

"""
Metoda explicit wait pozwala na definiowanie własnego warunku, co tu zostanie wykonane - jako parametr 
metody until.
Używamy wyrażenia lambda jako argumentu.
Zwróci False jeżeli warunek nie zostanie spełniony.
"""

wait = WebDriverWait(driver, 10)
driver.get("file:///home/wojtek/PycharmProjects/selenium_udemy/Selenium_files/Waits2.html")
driver.find_element_by_id("clickOnMe").click()
wait.until(lambda wd: len(wd.find_elements_by_tag_name("p")) == 1)

# jezeli zmienic dlugosc na 2, to test nie przejdzie, bo dlugosc listy to 1 a nie 2
# wiec test wyrzuci TimeoutException z racji przekroczenia czasu oczekiwania na zakonczenie testu:

# wait.until(lambda wd: len(wd.find_elements_by_tag_name("p")) == 2)

print(driver.find_element_by_tag_name("p").text)


"""
Inne podejscie z lambdą:
Aby stworzyć własny warunek dla WebDriverWait możemy również stworzyć klasę zawierającą metodę __call__ 
która jako parametr przyjmuje drivera i zawiera w swoim ciele warunek który będzie sprawdzany:

class WaitForListSize:
    def __init__(self, locator, expected_size):
        self.locator = locator
        self.expected_size = expected_size
    
    def __call__(self, driver):
        return len(driver.find_elements_by_xpath(self.locator)) == self.expected.size

Aby skorzystać z takiej metody w naszym WebDriverWait do metody until() przekazujemy obiekt klasy 
WaitForListSize:
    
    driver = webdriver.Chrome(ChromeDriverManager().install())
    wait = WebDriverWait(driver, 10)
    driver.get("file:///home/wojtek/PycharmProjects/selenium_udemy/Selenium_files/Waits2.html")
    driver.find_element_by_id("clickOnMe").click()
    wait.until(WaitForListSize("//p", 1))
    print(driver.find_element_by_tag_name("p").text)    
"""
