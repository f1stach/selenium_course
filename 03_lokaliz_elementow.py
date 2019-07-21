from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("file:///home/wojtek/PycharmProjects/selenium_udemy/Selenium_files/Test.html")
driver.maximize_window()

# szuakmy po id - z Test.html bierzemy przycisk Kliknij mnie - id: clickOnMe
driver.find_element(By.ID, "clickOnMe")
driver.find_element_by_id("clickOnMe")

# szukamy po nazwie - ponownie dla pola tekstowego fname:
driver.find_element_by_name("fname")

# szukamy po pełnym tekście linka w tagu <a>
driver.find_element_by_link_text("Visit W3Schools.com!")

# szukamy po częściowym tekście linka w tagu <a>
driver.find_element_by_partial_link_text("Visit W3Schools")

# szukamy po nazwie klasy - w test.html ukryty element w tagu <p>. Tag ten może posiadać
# więcej niż 1 klasę
driver.find_element_by_class_name("topSecret")
# driver.find_element_by_class_name("druga")

# szukamy po nazwie tagu
driver.find_element_by_tag_name("a")
driver.find_element_by_tag_name("p")
# driver.find_element_by_tag_name("div") # error - tag niedostepny w html
driver.find_element_by_tag_name("label")


# lokalizacja po selektorze css:
driver.find_element_by_css_selector("a")
driver.find_element_by_css_selector("img#smileImage") # tag img o id="smileImage"
driver.find_element_by_css_selector("p.topSecret") # tag p o klasie topSecret
print(driver.find_element_by_css_selector("th:first-child").text) # wypisujemy wartość wewn. th (tabela - pierwszy element)


# lokalizacja za pomocą XPath (wykorzystamy gdy nie ma opcji szukania po id czy name) - pełna ścieżka:
driver.find_element_by_xpath("/html/body/table/tbody/tr/th")
driver.find_element_by_xpath("//tbody//th") # //th - przechodzimy przez całą strukturę tbody aby znaleźć th
driver.find_element_by_xpath("//th")
driver.find_element_by_xpath("//th[text()='Month']")
driver.find_element_by_xpath("//button[@id='clickOnMe']")
# element table, który znajduje się po input. Przy małpie id mozna zmienić na name:
driver.find_element_by_xpath("//input[@id='fname']/following-sibling::table")


# listy tagów na stronie, gdy jest więcej niż jeden danego rodzaju tagów - find_elements
elements_list_length = len(driver.find_elements_by_xpath("//th"))
print(elements_list_length)


driver.quit()
