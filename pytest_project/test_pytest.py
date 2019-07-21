import pytest

"""
Nazwa pliku z testami musi zawierać słowo test w nazwie - na pocz. lub na koncu.
Metody w pliku testowym muszą zaczynać się od słowa test, aby zostały uruchomione.

Asercje sprawdzają czy zakładany warunek jest true

W naszym przykładzie sprawdzamy czy wynik dodawania jest True, a jeżeli nie to wyświetlamy
tekst po przecinku.

Porównujemy wszystko w sposób, który zwróci true lub false.

?ozna też porównywać stringi, np. tytuł strony z jakimś stringiem itp.
def test_text():
    assert driver.title == "Tom"

"""

def test_method():
    x = 5
    y = 2
    assert x+y == 7, "Assertion failed. Expected 7"
    assert x+y == 2, "Assertion failed. Expected 7"


def test_method_2():
    x = 5
    y = 2
    assert x+y == 7, "Assertion failed. Expected 7"
    assert x+y == 7, "Assertion failed. Expected 7"


# warto dorzucić więcej informacji do asercji aby rozszyfrować co mogło pójsc nie tak:
def test_method_3():
    x = 5
    y = 2
    assert x + y == 5, "Assertion failed. Expected 5 but was " + str(x+y)
    assert x + y == 7, "Assertion failed. Expected 7"

