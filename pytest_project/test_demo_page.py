"""
W pliku tym umieścimy fixture. Utworzenie przeglądarki będzie wykonane przed metodą
testową a po metodzie przeglądarka zostanie zamknięta.
"""

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


# tworzymy przeglądarkę i dołączamy fixture, który spowoduje, że metoda zostanie
# wywołana przed metodą testową:
@pytest.fixture()
def test_setup():
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("file:///home/wojtek/PycharmProjects/selenium_udemy/Selenium_files/FileUpload.html")
    driver.maximize_window()

    # definiujemy to co ma zostać wykonane przed i po metodzie testowej - słowo yield:
    yield
    driver.quit()


# sprawdzamy tytuł strony; podajemy nazwę metody z dekoratorem fixture w argumencie
# metody testowej, aby zaznaczyć, że ma wykonać się najpierw:
def test_method(test_setup):
    assert driver.title == "Strona testowa"


# udowadniamy, że metoda z dekoratorem uruchomi się pierwsza drugi raz przed kolejną
# metodą testową:
def test_method2(test_setup):
    assert driver.title == "Strona testowa"
