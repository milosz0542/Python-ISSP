import pandas as pd
import xml.etree.ElementTree as ET

# Get data from XML file
tree = ET.parse('kursy.xml')
root = tree.getroot()

# Store data in DataFrame
data = []
for pozycja in root.findall('pozycja'):
    kod_waluty = pozycja.find('kod_waluty').text
    kurs_sredni = pozycja.find('kurs_sredni').text.replace(',', '.')
    data.append([kod_waluty, float(kurs_sredni)])
df = pd.DataFrame(data, columns=['Currency', 'Rate'])

# Add PLN to the DataFrame
df.loc[len(df.index)] = ['PLN', 1.0]

# Save DataFrame to CSV file
df.to_csv('kursy.csv', index=False)

# Show currencies codes
print('Available currencies:')
for currency in df['Currency']:
    print(currency, end=' ')
print("\n")

# Get 2 currencies symbols from user
currency1 = input('Enter the first currency symbol: ')
currency2 = input('Enter the second currency symbol: ')

# Check if the currencies are in the DataFrame
if currency1 not in df['Currency'].values or currency2 not in df['Currency'].values:
    print('Invalid currency symbol')
    exit()

# Get the rates of the currencies
rate1 = df[df['Currency'] == currency1]['Rate'].values[0]
rate2 = df[df['Currency'] == currency2]['Rate'].values[0]

# Calculate the exchange rate
exchange_rate = rate1 / rate2

# Print the exchange rate
print(f'1 {currency1} = {exchange_rate} {currency2}')