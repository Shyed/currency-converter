# Import requests library for API calls
import requests

# API key and base URL for exchange rate API
API_KEY = "a9aa5c0977641cbeefb37ec3"
BASE_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair"

# Function to convert currency
def convert_currency(amount, base_currency, target_currency):
    # Build API URL with selected currencies and amount
    url = f"{BASE_URL}/{base_currency.upper()}/{target_currency.upper()}/{amount}"

    try:
        # Send GET request to API
        response = requests.get(url)

        # Convert response to JSON
        data = response.json()

        # Check if request was successful
        if data["result"] == "success":
            return data["conversion_result"]
        else:
            print("Error:", data.get("error-type", "Unknown error"))
            return None

    # Handle network/API errors
    except Exception as e:
        print("Network error:", e)
        return None


# Main CLI program
if __name__ == "__main__":
    print("=== Currency Converter ===")

    try:
        # Get user input
        amount = float(input("Enter amount to convert: "))
        base = input("Convert from (currency code, e.g. USD): ").strip()
        target = input("Convert to (currency code, e.g. EUR): ").strip()

        # Call conversion function
        result = convert_currency(amount, base, target)

        # Display result if successful
        if result is not None:
            print(f"\n{amount:.2f} {base.upper()} = {result:.2f} {target.upper()}")

    # Handle invalid numeric input
    except ValueError:
        print("Invalid input. Please enter a numeric amount.")
