'''
Klasa Student zawierająca:
- pola:
* imie i nazwisko
* nr_indeksu
* słownik, którego kluczami są nazwy przedmiotów, a wartościami oceny z przedmiotu
- metody:
* dodaj_ocene(przedmiot, ocena) - dodaje przedmiot i oceny do słownika
* srednia() - zwraca średnią ocen zapisując ją jako atrubut klasy
'''

class Student:
    def __new__(cls, imie, nazwisko, nr_indeksu):
        instance = super(Student, cls).__new__(cls)
        instance.imie = imie
        instance.nazwisko = nazwisko
        instance.nr_indeksu = nr_indeksu
        instance.oceny = {}
        return instance

    def dodaj_ocene(self, przedmiot, ocena):
        if przedmiot in self.oceny:
            self.oceny[przedmiot].append(ocena)
        else:
            self.oceny[przedmiot] = [ocena]

    def srednia(self):
        sum = 0
        count = 0
        for oceny in self.oceny.values():
            for ocena in oceny:
                sum += ocena
                count += 1
        return sum / count

def test_student():
    student = Student("Jan", "Kowalski", 12345)
    print(f"Student: {student.imie} {student.nazwisko}, nr indeksu: {student.nr_indeksu}")

    student.dodaj_ocene("Matematyka", 5)
    student.dodaj_ocene("Fizyka", 4)
    student.dodaj_ocene("Informatyka", 3)

    assert student.srednia() == 4, f"Expected 4, got {student.srednia()}"

    student.dodaj_ocene("Matematyka", 4)
    student.dodaj_ocene("Fizyka", 3)
    student.dodaj_ocene("Informatyka", 2)

    assert student.srednia() == 3.5, f"Expected 3.5, got {student.srednia()}"
    print("All tests passed.")

test_student()