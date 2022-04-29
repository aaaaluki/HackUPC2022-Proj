#!/usr/bin/env python3

import psycopg2


DEBUG = True

DB_HOST = 'localhost'
DB_NAME = 'moto'
DB_USER = 'postgres'
DB_PASS = None

ID = 0
NAME = 1
BRAND_ID = 2
YEAR = 3
FUEL = 4
PRICE = 5

QUERY_ID = 100


def get_moto(cur, qid):
    # Get all cols for the specified moto
    cur.execute('SELECT * FROM versions WHERE id = {};'.format(qid))
    moto = cur.fetchone()
    cur.execute('SELECT name FROM brands WHERE id = {};'.format(moto[BRAND_ID]))
    brand = cur.fetchone()

    if DEBUG:
        print('ID: {}'.format(moto[ID]))
        print('NAME: {}'.format(moto[NAME]))
        print('BRAND: {}'.format(brand[0]))
        print('BRAND_ID: {}'.format(moto[BRAND_ID]))
        print('YEAR: {}'.format(moto[YEAR]))
        print('FUEL: {}'.format(moto[FUEL]))
        print('PRICE: {}'.format(moto[PRICE]))


def main():
    # Connect to DB
    conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS)

    # Create a cursor
    cur = conn.cursor()

    # Execute a statement
    get_moto(cur, QUERY_ID)

    # Close the communication with the PostgreSQL
    cur.close()


if __name__ == '__main__':
    main()

