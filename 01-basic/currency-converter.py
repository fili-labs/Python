import requests

class CurrencyConverter:
    def __init__(self, url):
        # Fetching real-time data from the API
        data = requests.get(url).json()
        self.rates = data["rates"]

    def convert(self, from_currency, to_currency, amount):
        """Convert amount from one currency to another."""
        initial_amount = amount
        
        # Convert from non-EUR currency to EUR first
        if from_currency != 'EUR':
            amount = amount / self.rates[from_currency]
        
        # Convert from EUR to target currency
        amount = round(amount * self.rates[to_currency], 2)
        print(f"{initial_amount} {from_currency} = {amount} {to_currency}")

# Driver code
if __name__ == "__main__":
    YOUR_ACCESS_KEY = "Your API key here"
    url = f"http://data.fixer.io/api/latest?access_key={YOUR_ACCESS_KEY}"
    
    converter = CurrencyConverter(url)
    from_currency = input("From Currency (e.g., USD): ").upper()
    to_currency = input("To Currency (e.g., INR): ").upper()
    amount = float(input("Amount: "))
    
    converter.convert(from_currency, to_currency, amount)
