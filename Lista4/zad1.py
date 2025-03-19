'''
Klasa CiagGeometryczny
Inicjaizacja za pomocą metody __new__ wymaga wprowadzenia 3 argumentów:
- pierwszy wyraz ciągu
- iloraz ciągu
- ilość wyrazów ciągu

Klasa początkowo przechowuje n pierwszych wyrazów ciągu
Klasa posiada metody:
- add(n) - dodaje n kolejnych wyrazów ciągu
- print() - wypisuje wszystkie wyrazy ciągu
- sum() - zwraca sumę wszystkich wyrazów ciągu
- len() - zwraca ilość wyrazów ciągu
'''
import io
import sys


class CiagGeometryczny:
    def __new__(cls, *args, **kwargs):
        if len(args) != 3:
            raise ValueError("Podano złą ilość argumentów")
        return super().__new__(cls)

    def __init__(self, a1, q, n):
        self.a1 = a1
        self.q = q
        self.n = n
        self.ciag = [a1 * q**i for i in range(n)]

    def add(self, n):
        self.n += n
        self.ciag += [self.a1 * self.q**i for i in range(self.n)]

    def print(self):
        print(self.ciag)

    def sum(self):
        return sum(self.ciag)

    def len(self):
        return len(self.ciag)

def test():
    ciag = CiagGeometryczny(1, 2, 5)

    captured_output = io.StringIO()
    sys.stdout = captured_output

    ciag.print()

    result = captured_output.getvalue().strip()
    sys.stdout = sys.__stdout__

    expected_output = "[1, 2, 4, 8, 16]"
    assert result == expected_output, f"Expected [1, 2, 4, 8, 16], got {result}"

    assert ciag.sum() == 31, f"Expected 31, got {ciag.sum()}"

    assert ciag.len() == 5, f"Expected 5, got {ciag.len()}"

    ciag.add(3)

    assert ciag.sum() == 286, f"Expected 286, got {ciag.sum()}"
    print("All tests passed")

test()
