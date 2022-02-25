import json
from six.moves import urllib
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="mcclur36",
    password="1Oldumbrella!",
    database="messario"
)

mycursor = mydb.cursor()

url = "https://data.messari.io/api/v1/news"
res = urllib.request.urlopen(url)
with open('DougOutput.json') as json_file:
    data = json.load(json_file)
    print(data)
    for r in data['data']:
        id = r['id']
        title = r['title']
        content = r['content']
        tags = r['tags']
        published_at = r['published_at']
        url = r['url']

        sql1 = "DROP TABLE IF EXISTS news"
        sql2 = "CREATE TABLE news (id varchar(255), title varchar(255), content TEXT, url varchar(255))"
        sql3 = "INSERT INTO news (id, title, content, url) VALUES (%s, %s, %s, %s)"
        val = (id, title, content, url)
        # mycursor.execute(sql1)
        # mycursor.execute(sql2)
        mycursor.execute(sql3, val)

        mydb.commit()

    print("records inserted")