import json, sys, urllib.request

if len(sys.argv) != 3:
    print("Usage: ./currency.py lookup_currency base_currency. Example: ./currency.py cad usd")
    sys.exit()

currency = sys.argv[1]
baseCurrency = sys.argv[2]

currencyURL = "http://freecurrencyrates.com/api/action.php?do=cvals&iso=" + currency + "&f=" + baseCurrency + "&v=1&s=cbr"
f = urllib.request.urlopen(currencyURL)
obj = json.loads(f.read())
result = "1 " + currency.upper() + " is "
result += "{:,.2f}".format(1 / obj[currency.upper()]) + " " + baseCurrency.upper()

print(result)
