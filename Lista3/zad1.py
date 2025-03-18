'''
Klasa Egzamin zawiera słownik ocen, gdzie kluczem jest student, a wartością lista ocen.
Klasa posiada metody:
- Konstruktor, który tworzy pusty słownik ocen.
- DodajStudenta, który dodaje studenta i ocenę.
- UsunStudenta, który usuwa studenta.
- DrukujStudentow, który drukuje studentów wraz z ich ocenami (posortowanymi).
'''

class Egzamin:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Egzamin, cls).__new__(cls)
            cls.instance.grades = {}
        return cls.instance

    def DodajStudenta(self, student, grade):
        if student in self.grades:
            self.grades[student].append(grade)
        else:
            self.grades[student] = [grade]

    def UsunStudenta(self, student):
        if student in self.grades:
            del self.grades[student]

    def DrukujStudentow(self):
        for student in sorted(self.grades.keys()):
            print(f"{student}: {self.grades[student]}")

egzamin = Egzamin()
egzamin.DodajStudenta('Jan', 5)
egzamin.DodajStudenta('Anna', 4)
egzamin.DodajStudenta('Jan', 3)
egzamin.DodajStudenta('Anna', 5)
egzamin.DodajStudenta('Jan', 2)
egzamin.DrukujStudentow()
print()
egzamin.UsunStudenta('Jan')
egzamin.DrukujStudentow()