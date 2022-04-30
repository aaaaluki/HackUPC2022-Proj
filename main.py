#!/usr/bin/env python3
import sys

import pandas as pd
import psycopg2

from config import *


QUERY_ID = 100


def setup():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        sys.exit(1)

    cursor = conn.cursor()

    try:
        cursor.execute('SELECT * FROM versions;')
        versions = cursor.fetchall()
        df_versions = pd.DataFrame(versions)

        cursor.execute('SELECT * FROM brands;')
        brands = cursor.fetchall()
        df_brands = pd.DataFrame(brands)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        cursor.close()
        sys.exit(1)

    cursor.close()

    return df_brands, df_versions


def main(df_brands, df_versions):
    idx = df_versions[ID] == QUERY_ID
    query = df_versions[idx]
    brand = df_brands[df_brands[ID] == query[BRAND_ID].values[0]]
    print(query)


if __name__ == "__main__":
    df_brands, df_versions = setup()
    main(df_brands, df_versions)

