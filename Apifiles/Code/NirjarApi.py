import finnhub
import json
finnhub_client = finnhub.Client(api_key="c83f31qad3ift3bm8f7g")

print(finnhub_client.crypto_candles('BINANCE:BTCUSDT', 'D', 1590988249, 1591852249))
res = finnhub_client.crypto_candles('BINANCE:BTCUSDT', 'D', 1590988249, 1591852249)
data = json.dumps(res)
f = open("NirjarOutput.json", "w")
f.write(data)
f.close()

# open and read the file after the appending:
f = open("NirjarOutput.json", "r")
print(f.read())
