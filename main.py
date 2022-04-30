#!/usr/bin/env python3

import grafiques
import dbfilter
from config import *
from dbwrapper import DBWrapper
from dbfilter import DBFilter


def main():
    wrapper = DBWrapper(DB_HOST, DB_NAME, DB_USER, DB_PASS, DB_PORT)

    # Some sample data
    query = wrapper.get_moto(123)
    print('Query:\n{}'.format(wrapper.moto2str(query)))

    # Some matching data
    filters = []
    filters.append(DBFilter(NAME, dbfilter.EQ, 'R 100 RT   (1978-1996)'))
#    filters.append(DBFilter(YEAR, dbfilter.EQ, 1991))
#    filters.append(DBFilter(PRICE, dbfilter.LT, 6000))
#    filters.append(DBFilter(YEAR, dbfilter.GE, 2000))
    matches = wrapper.apply_filters(filters)

    # Display data
    fig = grafiques.graficar(wrapper, matches, query)


if __name__ == '__main__':
    main()
