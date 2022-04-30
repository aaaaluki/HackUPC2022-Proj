import sys

import pandas as pd
import psycopg2

from config import *


class DBWrapper:

    def __init__(self, h, db, usr, pas, p):
        try:
            conn = psycopg2.connect(
                host=h,
                database=db,
                user=usr,
                password=pas,
                port=p)
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

        self.df_brands = df_brands
        self.df_versions = df_versions

    def get_moto(self, qid):
        idx = self.df_versions[ID] == qid
        query = self.df_versions[idx]
        brand = self.df_brands[self.df_brands[ID] == query[BRAND_ID].values[0]]

        return query.values[0]

    def filter_by_param(self, param, param_name, sort_param=PRICE):
        idx = self.df_versions[param] == param_name
        query = self.df_versions[idx].values
        sorted_query = query[query[:, sort_param].argsort()]

        return sorted_query