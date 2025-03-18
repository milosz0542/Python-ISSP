'''
Klasa ułamek z metodami
skróć
(statyczne) - dodaj, odejmij, pomnóż, podziel
'''

class Ulamek:
    def __new__(cls, licznik, mianownik):
        instance = super(Ulamek, cls).__new__(cls)
        instance.licznik = licznik
        instance.mianownik = mianownik
        return instance

    def skroc(self):
        for i in range(2, min(self.licznik, self.mianownik) + 1):
            while self.licznik % i == 0 and self.mianownik % i == 0:
                self.licznik //= i
                self.mianownik //= i

    @staticmethod
    def dodaj(u1, u2):
        licznik = u1.licznik * u2.mianownik + u2.licznik * u1.mianownik
        mianownik = u1.mianownik * u2.mianownik
        result = Ulamek(licznik, mianownik)
        result.skroc()
        return result

    @staticmethod
    def odejmij(u1, u2):
        licznik = u1.licznik * u2.mianownik - u2.licznik * u1.mianownik
        mianownik = u1.mianownik * u2.mianownik
        result = Ulamek(licznik, mianownik)
        result.skroc()
        return result

    @staticmethod
    def pomnoz(u1, u2):
        licznik = u1.licznik * u2.licznik
        mianownik = u1.mianownik * u2.mianownik
        result = Ulamek(licznik, mianownik)
        result.skroc()
        return result

    @staticmethod
    def podziel(u1, u2):
        licznik = u1.licznik * u2.mianownik
        mianownik = u1.mianownik * u2.licznik
        result = Ulamek(licznik, mianownik)
        result.skroc()
        return result

def test_ulamek():
    u1 = Ulamek(1, 2)
    u2 = Ulamek(2, 3)

    # Test addition
    result = Ulamek.dodaj(u1, u2)
    assert result.licznik == 7 and result.mianownik == 6, f"Expected (7, 6), got ({result.licznik}, {result.mianownik})"

    # Test subtraction
    result = Ulamek.odejmij(u1, u2)
    assert result.licznik == -1 and result.mianownik == 6, f"Expected (-1, 6), got ({result.licznik}, {result.mianownik})"

    # Test multiplication
    result = Ulamek.pomnoz(u1, u2)
    assert result.licznik == 1 and result.mianownik == 3, f"Expected (1, 3), got ({result.licznik}, {result.mianownik})"

    # Test division
    result = Ulamek.podziel(u1, u2)
    assert result.licznik == 3 and result.mianownik == 4, f"Expected (3, 4), got ({result.licznik}, {result.mianownik})"

    print("All tests passed.")

# Run the tests
test_ulamek()