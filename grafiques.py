import numpy as np
import matplotlib.pyplot as plt

from config import *


# Funcio que grafica les variables
# ---*matrix es la matriu amb totes les motos on cada columna es
# ---una variable
# ---preu_moto es el preu de la moto que correspon al id que hem
# ---*seleccionat previament

def graficar(matrix, moto):
    prices = matrix[:,PRICE]
    name = matrix[:,NAME]
    year = matrix[:,YEAR]
    brand = matrix[:,BRAND_ID]
    fuel = matrix[:,FUEL]

    fig, axs = plt.subplots(2, 2, constrained_layout=True)

    axs[0, 0].scatter(name, prices)
    axs[0, 0].plot(moto[PRICE], linewidth=10)
    axs[0, 0].set_title('Model == name')
    axs[0, 0].set_ylabel('Preu (€)')        
    axs[0, 0].get_xaxis().set_visible(False)

    axs[0, 1].scatter(year, prices)
    axs[0, 1].plot(moto[PRICE], linewidth=10)
    axs[0, 1].set_title('any')
    axs[0, 1].set_ylabel('Preu (€)') 
    axs[0, 1].set_xlim([min(moto[YEAR]), max(max[YEAR])])   
    axs[0, 1].get_xaxis().set_visible(True)

    axs[1, 0].scatter(brand, prices)
    axs[1, 0].plot(moto[PRICE], linewidth=10)
    axs[1, 0].set_title('marca == brand')
    axs[1, 0].set_ylabel('Preu (€)')
    axs[1, 0].get_xaxis().set_visible(False)

    axs[1, 1].scatter(fuel, prices)
    axs[1, 1].plot(moto[PRICE], linewidth=10)
    axs[1, 1].set_title('gasolina')
    axs[1, 1].set_ylabel('Preu (€)')
    axs[0, 1].set_xlim([min(moto[FUEL]), max(max[FUEL])])         
    axs[1, 1].get_xaxis().set_visible(True)

    fig.suptitle('Comparació multiparamètrica ', fontsize=20)
    plt.xlim([1990, 2022])
    plt.show()
    return fig
