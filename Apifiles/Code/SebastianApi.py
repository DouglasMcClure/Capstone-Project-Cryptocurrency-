import requests
import json
import sqlite3
from sqlite3 import Error


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
    cur.execute("SELECT * FROM coinlore_coin_market")

    rows = cur.fetchall()

    for row in rows:
        print(row)

    with open('SebastianOutput.json') as json_file:
        data = json.load(json_file)
        print(data)
        sql1 = 'DROP TABLE IF EXISTS coinlore_coin_market'
        sql2 = 'CREATE TABLE coinlore_coin_market (name varchar(255), base varchar(255), quote varchar(255), ' \
               'price float, price_usd float, volume float, volume_usd float, time timestamp) '
        sql3 = 'INSERT OR REPLACE INTO coinlore_coin_market VALUES (?, ?, ?, ?, ?, ?, ?, ?)'
        cur.execute(sql1)
        cur.execute(sql2)
        for r in data:
            name = r['name']
            base = r['base']
            quote = r['quote']
            price = r['price']
            price_usd = r['price_usd']
            volume = r['volume']
            volume_usd = r['volume_usd']
            time = r['time']
            val = (name, base, quote, price, price_usd, volume, volume_usd, time)
            conn.commit()
            cur.execute(sql3, val)
            conn.commit()

        print("data inserted")
        cur.close()


def main():
    file = "capstonedatabase.sqlite"
    response = requests.get("https://api.coinlore.net/api/coin/markets/?id=90")
    res = json.dumps(response.json())
    f = open("SebastianOutput.json", "w")
    f.write(res)
    f.close()
    print(res)
    # create a database connection
    conn = create_connection(file)

    # insert data into database
    with conn:
        select_all_tasks(conn)


if __name__ == '__main__':
    main()