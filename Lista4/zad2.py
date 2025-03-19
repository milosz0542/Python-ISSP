'''
Klqsa KursyWalut przelicza kursy walut
Inicializacja klasy jest tworzona za pomocą metody __new__ i wymaga podania ścieżki do pliku z kursami walut:

Klasa posiada metody:
- przelicz(kwota, waluta1, waluta2) - przelicza kwotę z waluty1 na walutę2
- print() - wypisuje wszystkie kursy walut
- przeliczPLN(kwota, waluta) - przelicza kwotę z waluty na PLN
'''

import pandas as pd
import xml.etree.ElementTree as ET
import sys

class KursyWalut:
    def __new__(cls, path):
        instance = super(KursyWalut, cls).__new__(cls)
        instance.path = path
        instance.data = cls.get_data(path)
        return instance

    @staticmethod
    def get_data(path):
        tree = ET.parse(path)
        root = tree.getroot()

        data = []
        for pozycja in root.findall('pozycja'):
            kod_waluty = pozycja.find('kod_waluty').text
            kurs_sredni = pozycja.find('kurs_sredni').text.replace(',', '.')
            data.append([kod_waluty, float(kurs_sredni)])
        df = pd.DataFrame(data, columns=['Currency', 'Rate'])
        df.loc[len(df.index)] = ['PLN', 1.0]
        return df

    def przelicz(self, kwota, waluta1, waluta2):
        if waluta1 not in self.data['Currency'].values or waluta2 not in self.data['Currency'].values:
            return 'Invalid currency symbol'
        rate1 = self.data[self.data['Currency'] == waluta1]['Rate'].values[0]
        rate2 = self.data[self.data['Currency'] == waluta2]['Rate'].values[0]
        exchange_rate = rate1 / rate2
        return kwota * exchange_rate

    def print(self):
        print(self.data)

    def przeliczPLN(self, kwota, waluta):
        if waluta not in self.data['Currency'].values:
            return 'Invalid currency symbol'
        rate = self.data[self.data['Currency'] == waluta]['Rate'].values[0]
        return kwota * rate

kursy = KursyWalut("kursy.xml")
kursy.print()

try:
    option = int(input("Wybierz opcję:\n1 - przelicz\n2 - przeliczPLN\n"))
    if option == 1:
        kwota = float(input("Podaj kwotę: "))
        waluta1 = input("Podaj walutę 1: ")
        waluta2 = input("Podaj walutę 2: ")
        print(kursy.przelicz(kwota, waluta1, waluta2))
    elif option == 2:
        kwota = float(input("Podaj kwotę: "))
        waluta = input("Podaj walutę: ")
        print(kursy.przeliczPLN(kwota, waluta))
    else:
        print("Invalid option")
except ValueError:
    print("Invalid input")
    sys.exit(0)