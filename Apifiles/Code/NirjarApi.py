import finnhub
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
    cur.execute("SELECT * FROM finnhub_candles")

    rows = cur.fetchall()

    for row in rows:
        print(row)

    with open('NirjarOutput.json') as json_file:
        data = json.load(json_file)
        print(type(data))
        print(data)
        sql1 = 'DROP TABLE IF EXISTS finnhub_candles'
        sql2 = 'CREATE TABLE finnhub_candles (close_price float, high_price float, low_price float, open_price float, ' \
               'tstamp TIMESTAMP, volume_data float) '
        sql3 = 'INSERT OR REPLACE INTO finnhub_candles VALUES (?, ?, ?, ?, ?, ?)'
        cur.execute(sql1)
        cur.execute(sql2)
        i = 0
        for r in data:
            close_price = data['c'][i]
            print(close_price)
            high_price = data['h'][i]
            low_price = data['l'][i]
            open_price = data['o'][i]
            timestamp = data['t'][i]
            volume_data = data['v'][i]
            val = (close_price, high_price, low_price, open_price, timestamp, volume_data)
            conn.commit()
            cur.execute(sql3, val)
            conn.commit()
            i=i+1

        cur.close()


        print("records inserted")

def main():
    file = "capstonedatabase.sqlite"
    finnhub_client = finnhub.Client(api_key="c83f31qad3ift3bm8f7g")
    print(finnhub_client.crypto_candles('BINANCE:BTCUSDT', 'D', 1590988249, 1591852249))
    res = finnhub_client.crypto_candles('BINANCE:BTCUSDT', 'D', 1590988249, 1591852249)
    data = json.dumps(res)
    f = open("NirjarOutput.json", "w")
    f.write(data)
    f.close()

    # create a database connection
    conn = create_connection(file)

    with conn:
        select_all_tasks(conn)


if __name__ == '__main__':
    main()