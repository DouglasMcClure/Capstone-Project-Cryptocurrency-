import requests
import json

r = requests.get("https://nova.bitcambio.com.br/api/v3/public/getassets")
res = r.json()
print(res)
data = json.loads(r.text)
data = json.dumps(data)
f = open("SteveOutput.json", "w")
f.write(data)
f.close()

print(data)