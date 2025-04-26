class TaxCalculator:
    tax_rates = {
        "USA": 0.07,
        "CA": 0.05,
        "UK": 0.20,
        "DE": 0.19,
        "FR": 0.20,
        "IT": 0.22,
        "PL": 0.23,
    }
    def calculate_tax(self, country, amount):
        if country not in self.tax_rates:
            raise ValueError(f"Tax rate for {country} not found.")
        return amount * self.tax_rates[country]

    def add_country(self, country, tax_rate):
        self.tax_rates[country] = tax_rate
        print(f"Tax rate for {country} added: {tax_rate}")

tax_calculator = TaxCalculator()

print(tax_calculator.calculate_tax("PL", 420))
tax_calculator.add_country("ES", 0.21)
print(tax_calculator.calculate_tax("ES", 69))