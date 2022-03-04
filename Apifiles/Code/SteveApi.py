import requests
import sqlite3
from sqlite3 import Error
import json
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
    cur.execute("SELECT * FROM trade_assets")

    rows = cur.fetchall()

    for row in rows:
        print(row)

    with open('SteveOutput.json') as json_file:
        data = json.load(json_file)
        print(data)
        sql1 = 'DROP TABLE IF EXISTS trade_assets'
        sql2 = 'CREATE TABLE trade_assets (asset varchar(255), asset_long varchar(255), min_confirmation integer, ' \
               'withdraw_tx_fee float, withdraw_tx_fee_percent float, system_protocol varchar(255), decimal_places ' \
               'integer) '
        sql3 = 'INSERT OR REPLACE INTO trade_assets VALUES (?, ?, ?, ?, ?, ?, ?)'
        cur.execute(sql1)
        cur.execute(sql2)
        for r in data['result']:
            asset = r['Asset']
            asset_long = r['AssetLong']
            min_confirmation = r['MinConfirmation']
            withdraw_tx_fee = r['WithdrawTxFee']
            withdraw_tx_fee_percent = r['WithdrawTxFeePercent']
            system_protocol = r['SystemProtocol']
            decimal_places = r['DecimalPlaces']
            val = (asset, asset_long, min_confirmation, withdraw_tx_fee, withdraw_tx_fee_percent, system_protocol,
                   decimal_places)
            conn.commit()
            cur.execute(sql3, val)
            conn.commit()

        print("data inserted")
        cur.close()


def main():
    file = "capstonedatabase.sqlite"
    r = requests.get("https://nova.bitcambio.com.br/api/v3/public/getassets")
    res = r.json()

    # create a database connection
    conn = create_connection(file)

    # insert data into database
    with conn:
        select_all_tasks(conn)


if __name__ == '__main__':
    main()
