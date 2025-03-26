"""
Klasa RealNumbers. Przyjmuje ona listę zawierającą liczby rzeczywiste.
Zwraca sumę wszystkich par liczb z listy.

Autor: Miłosz Grześkowiak
Informatyka Stosowana i Systemy Pomiarowe, Wydział Fizyki i Astronomii Uniwersytetu Wrocławskiego
"""

class RealNumbers:
    def __new__(cls, numbers):
        if not isinstance(numbers, list) or len(numbers) == 0:
            return None
        return super().__new__(cls)
    def __init__(self, numbers):
        self._numbers = numbers
    def add(self, number):
        self._numbers.append(number)
    def sum_table(self):
        """sum of all pairs of numbers in the list"""
        for i in range(len(self._numbers)):
            for j in range(i + 1, len(self._numbers)):
                print(f"{self._numbers[i] + self._numbers[j]}")


realnumbers = RealNumbers([1, 2, 3, 4, 5])

realnumbers.sum_table()
