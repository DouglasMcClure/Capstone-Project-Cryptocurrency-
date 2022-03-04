import json

import requests
from six.moves import urllib
import sqlite3
from sqlite3 import Error
import mysql.connector


def create_connection(db_file):
    """ create a database connection to the SQLite database
            specified by the db_file
        :param db_file: database file
        :return: Connection object or None
        """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def select_all_tasks(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM messario_news")

    rows = cur.fetchall()

    for row in rows:
        print(row)

    with open('DougOutput.json') as json_file:
        data = json.load(json_file)
        print(data)
        sql1 = 'DROP TABLE IF EXISTS messario_news'
        sql2 = 'CREATE TABLE messario_news (id varchar(255), title varchar(255), content text, published_at ' \
               'TIMESTAMP, url varchar(255)) '
        sql3 = 'INSERT OR REPLACE INTO messario_news VALUES (?, ?, ?, ?, ?)'
        cur.execute(sql1)
        cur.execute(sql2)
        for r in data['data']:
            id = r['id']
            title = r['title']
            content = r['content']
            published_at = r['published_at']
            url = r['url']
            val = (id, title, content, published_at, url)
            conn.commit()
            cur.execute(sql3, val)
            conn.commit()

        cur.close()


        print("records inserted")


def main():
    file = "capstonedatabase.sqlite"
    url = "https://data.messari.io/api/v1/news"
    res = urllib.request.urlopen(url)

    # create a database connection
    conn = create_connection(file)

    with conn:
        select_all_tasks(conn)


if __name__ == '__main__':
    main()
