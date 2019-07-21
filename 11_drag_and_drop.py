from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://demos.telerik.com/kendo-ui/dragdrop/index")

"""
Symulacja drag and drop.
"""

# lokalizujemy elementy - mniejsze kółko:
draggable = driver.find_element_by_id("draggable")

# lokalizujemy elementy - wieksze kółko:
drop_target = driver.find_element_by_id("droptarget")

# drag and drop za pomocą ActionChains - funkcja drag_and_drop(skąd, dokąd):
webdriver.ActionChains(driver).drag_and_drop(draggable, drop_target).perform()
