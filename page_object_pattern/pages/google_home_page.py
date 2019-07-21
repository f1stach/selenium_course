"""
Page Object Pattern
Wykorzystamy go po to, aby nie kopiować kodu dot. hoteli aby znaleźć dane dla innego
miasta, pasażera czy daty. Ponadto testy mogą failować z powodu zmiany nazw selektorów.
"""

# testujemy google search: w klasie w metodzie init definiujemy 2 selektory, które
# mają nazwy q i btnK (info z www google):


class GoogleHomePage:
    def __init__(self, driver):
        self.driver = driver
        self.search_input_name = 'q'
        self.search_button_name = 'btnK'

    def search_in_google(self, text):
        self.driver.find_element_by_name(self.search_input_name).send_keys(text)
        self.driver.find_element_by_name(self.search_button_name).click()
