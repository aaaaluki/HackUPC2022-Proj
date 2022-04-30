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

    # Returns all the data from the moto (id, name, brand_id, year, fuel, price)
    def get_moto(self, qid):
        idx = self.df_versions[ID] == qid
        query = self.df_versions[idx]

        return query.values[0]

    # By the brand_id returns the brand_name
    def get_brand(self, bid):
        return self.df_brands[self.df_brands[ID] == bid].values[0,1]

    # Applys multiple filters and returns the result as a sorted (PRICE by default) numpy.ndarray
    def apply_filters(self, filters, sort_param=PRICE):
        query = self.df_versions
        for f in filters:
            query = f.apply(query)

        query = query.values

        return query[query[:, sort_param].argsort()]

    # Coincidence search
    # Searches the coincidences in value of a certain parameter (name,year...) and returns all the coincidences
    # ordered by the sort parameter in increasing order
    def filter_by_param(self, param, param_name, sort_param=PRICE):
        idx = self.df_versions[param] == param_name
        query = self.df_versions[idx].values

        return query[query[:, sort_param].argsort()]

    # Moto to string
    def moto2str(self, sel):
        return 'ID: {}\nMODEL: {}\nBRAND: {}\nYEAR: {}\nFUEL: {}\nPRICE: {}'.format(sel[ID], sel[NAME],
                                                                                    self.get_brand(sel[BRAND_ID]),
                                                                                    sel[YEAR], sel[FUEL], sel[PRICE])
