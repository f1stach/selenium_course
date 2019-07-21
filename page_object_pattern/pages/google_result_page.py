"""
W tym pliku odzwierciedlamy stronę, która zwraca wyniki wyszukiwania.
"""


class GoogleResultPage:

    def __init__(self, driver):
        self.driver = driver
        self.search_results_xpath = "//h3[@class='LC201b']"

    def open_first_result(self):
        self.driver.find_elements_by_xpath(self.search_results_xpath)[0].click()
