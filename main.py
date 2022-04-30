#!/usr/bin/env python3

from config import *
from dbwrapper import DBWrapper


def main():
    wrapper = DBWrapper(DB_HOST, DB_NAME, DB_USER, DB_PASS, DB_PORT)
    # query = wrapper.get_moto(100)
    query = wrapper.filter_by_param(NAME, 'R 100 RT   (1978-1996)')

    print(query)


if __name__ == "__main__":
    main()

