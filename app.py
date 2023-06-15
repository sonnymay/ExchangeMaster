import requests

def get_exchange_rate(api_key, base_currency, target_currency):
    url = f"https://open.er-api.com/v6/latest/{base_currency}"
    
    # Making a GET request to the API
    response = requests.get(url)
    data = response.json()
    
    # Check if the response contains the rates
    if "rates" in data:
        return data["rates"].get(target_currency)
    else:
        return None

def convert_currency(amount, exchange_rate):
    return amount * exchange_rate

def main():
    # Insert your API key here
    api_key = "YOUR_API_KEY"

    # Input for base and target currencies
    base_currency = input("Enter the base currency (e.g. USD): ").upper()
    target_currency = input("Enter the target currency (e.g. EUR): ").upper()

    # Input for the amount to be converted
    amount = float(input(f"Enter the amount in {base_currency}: "))

    # Fetching the exchange rate
    exchange_rate = get_exchange_rate(api_key, base_currency, target_currency)

    if exchange_rate:
        # Converting the amount
        converted_amount = convert_currency(amount, exchange_rate)
        print(f"{amount} {base_currency} is equal to {converted_amount:.2f} {target_currency}.")
    else:
        print("Error: Unable to fetch the exchange rate.")

if __name__ == "__main__":
    main()
