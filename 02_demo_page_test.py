from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("file:///home/wojtek/PycharmProjects/selenium_udemy/Selenium_files/Test.html")
driver.maximize_window()
driver.find_element_by_id("newPage").click()

# quit - zamyka wszystkie okna otwarte przez selenium
# driver.quit()

# close - zamyka okno, na którym jest focus (tutaj to z test.html)
driver.close()
