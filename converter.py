import requests

API_KEY = "a9aa5c0977641cbeefb37ec3"
BASE_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair"

def convert_currency(amount, base_currency, target_currency):
    # Build full API URL with currencies and amount
    url = f"{BASE_URL}/{base_currency.upper()}/{target_currency.upper()}/{amount}"

    try:
        response = requests.get(url)
        data = response.json()

        # Check for success
        if data["result"] == "success":
            return data["conversion_result"]
        else:
            print("Error:", data.get("error-type", "Unknown error"))
            return None
    except Exception as e:
        print("Network error:", e)
        return None

# CLI interface
if __name__ == "__main__":
    print("=== Currency Converter ===")

    try:
        amount = float(input("Enter amount to convert: "))
        base = input("Convert from (currency code, e.g. USD): ").strip()
        target = input("Convert to (currency code, e.g. EUR): ").strip()

        result = convert_currency(amount, base, target)

        if result is not None:
            print(f"\n{amount:.2f} {base.upper()} = {result:.2f} {target.upper()}")
    except ValueError:
        print("Invalid input. Please enter a numeric amount.")
