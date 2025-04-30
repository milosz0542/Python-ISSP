class PlaszczyznaKartezjanska:
    def __new__(cls, punkty):
        instance = super(PlaszczyznaKartezjanska, cls).__new__(cls)
        instance.punkty = punkty
        return instance

    def __init__(self, punkty):
        self.punkty = punkty

    def dodaj_punkt(self, x, y):
        self.punkty.append(tuple([x, y]))

    def najwieksza_odleglosc(self):
        max_odleglosc = 0
        max_punkty = None
        for i in range(len(self.punkty)):
            for j in range(i + 1, len(self.punkty)):
                x1, y1 = self.punkty[i]
                x2, y2 = self.punkty[j]
                odleglosc = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
                if odleglosc > max_odleglosc:
                    max_odleglosc = odleglosc
                    max_punkty = (self.punkty[i], self.punkty[j])

        return max_odleglosc, max_punkty

    def zamien_miejscami(self, indeks):
        if indeks < 0 or indeks >= len(self.punkty):
            raise IndexError("Indeks poza zakresem")
        x = self.punkty[indeks][0]
        y = self.punkty[indeks][1]

        self.punkty[indeks] = (y, x)

    def __str__(self):
        return str(self.punkty)

    def __len__(self):
        return len(self.punkty)

if __name__ == "__main__":
    punkty = [(1, 2), (3, 4), (5, 6)]
    plaszczyzna = PlaszczyznaKartezjanska(punkty)
    print(plaszczyzna)

    plaszczyzna.dodaj_punkt(7, 8)

    print(plaszczyzna)
    print("Liczba punktów:", len(plaszczyzna))
    print("Największa odległość:", plaszczyzna.najwieksza_odleglosc())

    plaszczyzna.zamien_miejscami(1)
    print(plaszczyzna)