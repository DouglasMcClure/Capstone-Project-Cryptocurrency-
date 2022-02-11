import requests

response = requests.get("https://api.coinlore.net/api/tickers/ (First 100 Coins)")

response = requests.get("https://api.coinlore.net/api/coin/markets/?id=90")

print(response)
