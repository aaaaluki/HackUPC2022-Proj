#!/usr/bin/env python3
import dbfilter
from config import *
from dbwrapper import DBWrapper
from dbfilter import DBFilter


def Test():
    wrapper = DBWrapper(DB_HOST, DB_NAME, DB_USER, DB_PASS, DB_PORT)
    # query = wrapper.get_moto(100)
    # query = wrapper.filter_by_param(NAME, 'R 100 RT   (1978-1996)')
    filters = []
    filters.append(DBFilter(PRICE, dbfilter.LT, 6000))
    filters.append(DBFilter(PRICE, dbfilter.GE, 5990))
    query = wrapper.apply_filters(filters)
    
    #print(query)
    #print("+++++++++++++++++++++++++++query returned by Test_DB_Wrapper")
    return query


if __name__ == "__main__":
    Test()

