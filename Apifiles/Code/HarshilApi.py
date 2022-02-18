import cryptocompare
import requests
import json

cryptocompare.cryptocompare._set_api_key_parameter("cb3698c7826c7ff28f8cda185c994cccf398bcb7169a818433827ee347f45a8b")
r = requests.get("https://min-api.cryptocompare.com/data/top/exchanges/full?fsym=BTC&tsym=USD")
res = r.json()
print(res)
data = json.loads(r.text)
data = json.dumps(data)
f = open("HarshilOutput.json", "w")
f.write(data)
f.close()
