import pytest

"""
Skippowanie wybranych testów - dekorator skip

Oznaczanie metody jako kończącą się niepowodzeniem - dekorator xfail.
"""

# dekorator skip spowoduje, ze metoda zostanie pominięta:
@pytest.mark.xfail
def test_method():
    x = 5
    y = 2
    assert x+y == 7, "Assertion failed. Expected 7"
    assert x+y == 2, "Assertion failed. Expected 7"


@pytest.mark.skip
def test_method_2():
    x = 5
    y = 2
    assert x+y == 7, "Assertion failed. Expected 7"
    assert x+y == 7, "Assertion failed. Expected 7"


# warto dorzucić więcej informacji do asercji aby rozszyfrować co mogło pójsc nie tak:
def test_method_3():
    x = 5
    y = 2
    assert x + y == 7, "Assertion failed. Expected 5 but was " + str(x+y)
    assert x + y == 7, "Assertion failed. Expected 7"


"""
Odpalanie kilku testów jednoczesnie.

1. Instalujemy paczkę: pip install pytest-xdist
2. W terminalu wpisujemy np.: py.test -n 3 - chcemy jednoczesnie odpalic 3 testy.
Albo: py.test test_demo.py -n 2 - dwa testy równocześnie (współbieżnie) z pliku.
"""