import requests
import json
import mysql.connector

# mydb = mysql.connector.connect(
#     host="localhost",
#     user="lepore69",
#     password="1Redvegetable!",
#     database="bitcambio"
# )

# mycursor = mydb.cursor()
r = requests.get("https://nova.bitcambio.com.br/api/v3/public/getassets")
res = r.json()
print(res)
# for r in res['']:
#     id = r['id']
#     title = r['title']
#     content = r['content']
#     tags = r['tags']
#     published_at = r['published_at']
#     url = r['url']
#
#     sql1 = "DROP TABLE IF EXISTS news"
#     sql2 = "CREATE TABLE news (id varchar(255), title varchar(255), content TEXT, url varchar(255))"
#     sql3 = "INSERT INTO news (id, title, content, url) VALUES (%s, %s, %s, %s)"
#     val = (id, title, content, url)
#     # mycursor.execute(sql1)
#     # mycursor.execute(sql2)
#     mycursor.execute(sql3, val)
#
#     mydb.commit()
#
# print("records inserted")