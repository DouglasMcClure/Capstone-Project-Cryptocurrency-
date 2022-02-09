import finnhub
import pandas as pd
import requests

# base asset refers to the asset that is the quantity of a symbol.
# For the symbol BTCUSDT, BTC would be the base asset.
# quote asset refers to the asset that is the price of a symbol.
# For the symbol BTCUSDT, USDT would be the quote asset.

# Setup client
finnhub_client = finnhub.Client(api_key="c80ac2qad3i8n3bhdjt0")

r = requests.post('https://finnhub.io/api/v1/webhook/add?token=c80ac2qad3i8n3bhdjt0', json={'event': 'earnings', 'symbol': 'AAPL'})

# Stock candles
res = finnhub_client.crypto_candles(symbol, resolution, initialTimestamp, endingTimestamp)
print(res)

# Convert to Pandas Dataframe
print(pd.DataFrame(res))
