"""
Pokaz działania dekoratora pytest.mark.parametrize("nazwa argumentu", [(wartosc argumentu)])

Zadanie to parametryzacja argumentów, dla których będzie odpalana metoda testowa. Czyli zostanie odpalona
dla kilku różnych wartości argumentów.
"""

import pytest


# sprawdzamy czy wartosc dwóch składników jest równa wartoścu argumentu suma;
# lista tupli odpowiada wartościom argumentów składnik i suma. Czyli składnik ma 5 a suma 10
# a w drugim przypadku testowym skladnik ma 2 i suma 4.

@pytest.mark.parametrize("skladnik, suma", [(5,10), (2,4)])
def test_dodawanie(skladnik, suma):
    assert skladnik + skladnik == suma, "Suma dwoch takich samych skladnikow powinna byc rowna " + str(skladnik+skladnik)
