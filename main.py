import tkinter as tk
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)
import grafiques
from Test_DB_Wrapper import *
#import dbwrapper
#import dbfilter

""""
Aqui va la part del Lluc

"""


class Window(tk.Tk): 
    def __init__(self, matrix):
        super().__init__()
        self.title('Comparar motocicleta')
        moto = [28277, 'Primavera  125 3V Touring ABS (2014-2020)', 99, 2016, 2, 5997]
        figure_canvas = FigureCanvasTkAgg(grafiques.graficar(matrix, moto), self)
        NavigationToolbar2Tk(figure_canvas, self)



if __name__ == '__main__':
    test = Test()
    print(test)
    print("+++++++++++++++++++++++++++query returned by Test_DB_Wrapper")
    window=Window(test)
    window.mainloop()






