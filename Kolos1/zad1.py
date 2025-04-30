import pandas as pd
import xml.etree.ElementTree as ET
import sys


class ImperialConverter:
    """Klasa służąca do konwersji jednostek imperialnych - mile, yard, feet, inch na jednostki SI"""

    def __new__(cls, path):
        instance = super(ImperialConverter, cls).__new__(cls)
        instance.path = path
        instance.data = cls.get_data(path)
        return instance

    @staticmethod
    def get_data(path):
        tree = ET.parse(path)
        root = tree.getroot()

        data = []
        for unit in root.findall('Unit'):
            symbol = unit.find('Symbol').text
            value_in_meters = unit.find('ValueInMeters').text.replace(',', '.')
            data.append([symbol, float(value_in_meters)])
        df = pd.DataFrame(data, columns=['symbol', 'value_in_meters'])

        return df

    def przelicz_na_metry(self, jednostka, wartosc):
        if jednostka not in self.data['symbol'].values:
            return 'Niepoprawny symbol jednostki'
        wartosc_jednostki = self.data[self.data['symbol'] == jednostka]['value_in_meters'].values[0]
        return wartosc * wartosc_jednostki

    def przelicz(self, jednostka1, jednostka2, wartosc):
        if jednostka1 not in self.data['symbol'].values or jednostka2 not in self.data['symbol'].values:
            return 'Niepoprawny symbol jednostki'
        wartosc_jednostki1 = self.data[self.data['symbol'] == jednostka1]['value_in_meters'].values[0]
        wartosc_jednostki2 = self.data[self.data['symbol'] == jednostka2]['value_in_meters'].values[0]
        jednostka1_metry = wartosc * wartosc_jednostki1
        return jednostka1_metry / wartosc_jednostki2

    def print(self):
        print(self.data)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Podaj ścieżkę do pliku XML")
        path = input("/path/to/file: ")
    else:
        path = sys.argv[1]
    converter = ImperialConverter(path)
    converter.print()

    print("\n\n")

    # Przykładowe użycie
    print("Mile na metry:", converter.przelicz_na_metry('mi', 5))
    print("Mile na jardy:", converter.przelicz('mi', 'yd', 5))
