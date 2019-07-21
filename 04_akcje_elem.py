from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("file:///home/wojtek/PycharmProjects/selenium_udemy/Selenium_files/Test.html")
driver.maximize_window()

"""
klikanie na element;
można albo wywołać metodę na szukanym elemencie albo przypisać akcję do zmiennej
jeżeli zostawimy obie opcje to test wyrzuci alert, ponieważ będzie chciał wykonać 2x click na ten sam
przycisk a nie da rady, bo po jednym kliknieciu pokazuje się okienko z warningiem na stronie
"""
driver.find_element_by_id("clickOnMe").click()
# click_me_button = driver.find_element_by_id("clickOnMe")
# click_me_button.click()

"""
obsługa alertów.
Wywołujemy alert wrzucając poniżej drugi raz kliknięcie tego samego przycisku co wyżej.
Musimy dostać się do alertu poprzez metodę switch_to.alert
Po wpisaniu komend warto wykonać debuggowanie aby potwierdzić, że alerty są zamykane.
"""
# akceptujemy pierwszy alert po pierwszym naciśnięciu przycisku:
driver.switch_to.alert.accept()

driver.find_element_by_id("clickOnMe").click()

# każemy pominąć drugi alert po drugim naciśnięciu przycisku:
driver.switch_to.alert.accept()

"""
Wprowadzanie wartości do pola tekstowego (typ input).
Metoda send_keys("tekst")
"""
driver.find_element_by_id("fname").send_keys("Wojtek")

"""
Symulacja naciśnięcia Entera w polu tekstowym
Lokalizujemy input - pole tekstowe z hasłem
W metodzie send_keys wykorzystujemy klasę Keys (symulacja klawiszy) z metodą ENTER
"""
# driver.find_element_by_name("password").send_keys(Keys.ENTER)

"""
Wybieranie pozycji z menu select (lista rozwijana).
Na stronie 4 pozycje, szukamy Volvo, które jest widocznym tekstem (visible text).
"""
auto_select = Select(driver.find_element_by_tag_name("select"))
auto_select.select_by_visible_text("Volvo")

# teraz szukamy za pomocą pola value:
auto_select.select_by_value("saab")

# za pomocą indexu odpowiedniego - 0 to Volvo, 1 i kolejne to następne wpisy:
auto_select.select_by_index(0)

"""
Zaznaczanie checkboxa
"""
driver.find_element_by_xpath("//input[@type='checkbox']").click()

"""
Zaznaczanie radio button
"""
driver.find_element_by_xpath("//input[@value='male']").click()

"""
Pobieranie tekstu z elementu wenwatrz tagu HTML
"""
print(driver.find_element_by_xpath("//input[@value='male']").text) # nic się nie wyświetla, bo brak tekstu wewnątrz tagu
print(driver.find_element_by_tag_name("h1").text)
print(driver.find_element_by_id("clickOnMe").text)
print(driver.find_element_by_tag_name("p").text) # tekst z ukrytego taga nie pojawia się w outpucie

"""
Pobieranie tekstu z ukrytego elementu
Metoda getu_attribute("textContent") pobiera treść ukrytego elementu
"""
print(driver.find_element_by_tag_name("p").get_attribute("textContent"))

# za pomocą get_attribute można też pobrać to co wpisano w polu tekstowym:
print("Element text is " + driver.find_element_by_id("fname").get_attribute("value"))

"""
Sprawdzenie czy obrazek wyświetla się na stronie.
Robimy to poprzez sprawdzenie rozmiaru elementu typu obraz. 
Są dwie metody: size oraz get_attribute, ale lepiej korzystać z tej drugiej 
z argumentem "naturalHeight", bo pokazuje rozmiar obrazka, który faktycznie został wczytany.
"""
print(driver.find_element_by_id("smileImage").size.get("height"))
print(driver.find_element_by_id("smileImage").get_attribute("naturalHeight"))

"""
Przełączanie do nowo otwartego okna przeglądarki.
Domyślnie driver nie działa na nowo otwartej stronie w innym oknie (przycisk ClickMe).

Klikamy w teście na przycisk i wyświetlamy tytuł strony, na której jesteśmy.
Wyświetlił się tytuł pierwotnej strony testowej, nie nowo otwartej.
"""
driver.find_element_by_id("newPage").click()
print("We are in window named:", driver.title)

# lokalizujemy nowe okno:
current_window_name = driver.current_window_handle

# pobieramy wszystkie okna dostępne dla webdrivera:
window_names = driver.window_handles

# iterujemy po tych oknach i sprawdzamy czy kolejne okno z listy jest różne od obecnego.
# jeżeli tak to przełączamy.
for window in window_names:
    if window != current_window_name:
        driver.switch_to.window(window)

print("New window title is:", driver.title)

# przełączamy się ponownie do pierwotnego okna strony testowej:
driver.switch_to.window(current_window_name)
print("The window title is:", driver.title)



# driver.quit()