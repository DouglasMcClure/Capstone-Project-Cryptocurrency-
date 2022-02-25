import requests
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="castel58",
    password="1Gabbyghost!",
    database="coinlore"
)

mycursor = mydb.cursor()

response = requests.get("https://api.coinlore.net/api/coin/markets/?id=90")
res = response.json()
print(res)
for r in res:
    name = r['name']
    base = r['base']
    quote = r['quote']
    price = r['price']
    price_usd = r['price_usd']
    volume = r['volume']
    volume_usd = r['volume_usd']
    time = r['time']

    sql = "INSERT INTO coinmarket (name, base, quote, price) VALUES (%s,%s,%s,%f)"
    val = (name, base, quote, price)
    mycursor.execute(sql, val)

    mydb.commit()

print("records inserted")