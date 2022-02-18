import finnhub
finnhub_client = finnhub.Client(api_key="c83f31qad3ift3bm8f7g")

print(finnhub_client.crypto_candles('BINANCE:BTCUSDT', 'D', 1590988249, 1591852249))
