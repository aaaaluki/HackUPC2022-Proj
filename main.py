#!/usr/bin/env python3

import tkinter as tk
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)

import grafiques
import dbfilter
from config import *
from dbwrapper import DBWrapper
from dbfilter import DBFilter


class Window(tk.Tk):
    def __init__(self, matches, moto):
        super().__init__()
        self.title('Compare motomami')
        figure_canvas = FigureCanvasTkAgg(grafiques.graficar(matches, moto), self)
        NavigationToolbar2Tk(figure_canvas, self)


def main():
    wrapper = DBWrapper(DB_HOST, DB_NAME, DB_USER, DB_PASS, DB_PORT)

    # Some sample data
    query = wrapper.get_moto(123)

    filters = []
    filters.append(DBFilter(PRICE, dbfilter.LT, 6000))
    filters.append(DBFilter(YEAR, dbfilter.GE, 2000))
    matches = wrapper.apply_filters(filters)

    window = Window(matches, query)
    window.mainloop()


if __name__ == '__main__':
    main()
