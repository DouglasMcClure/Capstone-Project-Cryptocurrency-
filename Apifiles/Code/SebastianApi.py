import requests
import json

response = requests.get("https://api.coinlore.net/api/coin/markets/?id=90")
res = response.json()
print(res)
data = json.loads(response.text)
data = json.dumps(data)
print(data)