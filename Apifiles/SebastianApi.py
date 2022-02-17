import requests


response = requests.get("https://api.coinlore.net/api/coin/markets/?id=90")
res = response.json()
print(res)
