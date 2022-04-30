#!/usr/bin/env python3
import tkinter as tk
import matplotlib

import dbfilter
import grafiques
from config import *
from dbwrapper import DBWrapper
from dbfilter import DBFilter
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)
matplotlib.use('TkAgg')


class Window(tk.Tk):
    def __init__(self, matches, moto):
        super().__init__()
        self.title('Comparar motocicleta')
        figure_canvas = FigureCanvasTkAgg(
            grafiques.graficar(matches, moto), self)
        NavigationToolbar2Tk(figure_canvas, self)


def main():
    wrapper = DBWrapper(DB_HOST, DB_NAME, DB_USER, DB_PASS, DB_PORT)
    id_request = tk.Tk()
    entrada = tk.Entry(id_request)
    enter = tk.Button(id_request, text="Enter",
                      command=wrapper.get_moto(123))
    query=wrapper.get_moto(123)
    id_request.mainloop()

    filters = []
    filters.append(DBFilter(PRICE, dbfilter.LT, 6000))
    filters.append(DBFilter(YEAR, dbfilter.GE, 2000))
    matches = wrapper.apply_filters(filters)

    window = Window(matches, query)
    window.mainloop()


if __name__ == '__main__':
    main()
