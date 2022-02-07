import finnhub
import pandas as pd

# Setup client
finnhub_client = finnhub.Client(api_key="c80ac2qad3i8n3bhdjt0");
symbol = input()
resolution = input()
initialTimestamp = input()
endingTimestamp = input()
# Stock candles
res = finnhub_client.crypto_candles(symbol, resolution, initialTimestamp, endingTimestamp)
print(res);

#Convert to Pandas Dataframe
import pandas as pd
print(pd.DataFrame(res))