import requests

r = requests.get("https://nova.bitcambio.com.br/api/v3/public/getassets")
res = r.json()
print(res)
