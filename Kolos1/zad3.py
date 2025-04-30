# Łamaną zasadą SOLID jest to, że klasa powinna być otwarta na rozszerzenia

class WielokatForemny:
    def __init__(self, nazwa, bok):
        self.nazwa = nazwa
        self.bok = bok

    def oblicz_pole(self):
        raise NotImplementedError()

class Trojkat(WielokatForemny):
    def __init__(self, bok):
        super().__init__("Trojkat", bok)

    def oblicz_pole(self):
        return (self.bok ** 2) * (3 ** 0.5) / 4

class Kwadrat(WielokatForemny):
    def __init__(self, bok):
        super().__init__("Kwadrat", bok)

    def oblicz_pole(self):
        return self.bok ** 2




