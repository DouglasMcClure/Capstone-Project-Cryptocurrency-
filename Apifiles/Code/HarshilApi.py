import cryptocompare
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
    cur.execute("SELECT * FROM cryptocompare_coin_info")

    rows = cur.fetchall()

    for row in rows:
        print(row)

    with open('HarshilOutput.json') as json_file:
        data = json.load(json_file)
        print(data)
        sql1 = 'DROP TABLE IF EXISTS cryptocompare_coin_info'
        sql2 = 'CREATE TABLE cryptocompare_coin_info (id integer, name varchar(255), full_name varchar(255), ' \
               'image_url varchar(255), asset_launch_date DATE) '
        sql3 = 'INSERT OR REPLACE INTO cryptocompare_coin_info VALUES (?, ?, ?, ?, ?)'
        cur.execute(sql1)
        cur.execute(sql2)
        for i in data:
            id = data['Data']['CoinInfo']['Id']
            name = data['Data']['CoinInfo']['Name']
            full_name = data['Data']['CoinInfo']['FullName']
            image_url = data['Data']['CoinInfo']['ImageUrl']
            asset_launch_date = data['Data']['CoinInfo']['AssetLaunchDate']
            val = (id, name, full_name, image_url, asset_launch_date)
            conn.commit()
            cur.execute(sql3, val)
            conn.commit()

        print("data inserted")
        cur.close()


def main():
    file = "capstonedatabase.sqlite"
    cryptocompare.cryptocompare._set_api_key_parameter(
        "cb3698c7826c7ff28f8cda185c994cccf398bcb7169a818433827ee347f45a8b")
    r = requests.get("https://min-api.cryptocompare.com/data/top/exchanges/full?fsym=BTC&tsym=USD")
    res = r.json()
    data = json.dumps(res)
    f = open("HarshilOutput.json", "w")
    f.write(data)
    f.close()
    # create a database connection
    conn = create_connection(file)

    # insert data into database
    with conn:
        select_all_tasks(conn)


if __name__ == '__main__':
    main()