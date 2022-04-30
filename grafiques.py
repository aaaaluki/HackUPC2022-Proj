import matplotlib.pyplot as plt

from config import *


MOTO_COLOR = 'red'
MOTO_LW = 6


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
    axs[0, 0].scatter(moto[NAME], moto[PRICE], c=MOTO_COLOR, linewidth=MOTO_LW)
    axs[0, 0].set_title('Model == name')
    axs[0, 0].set_ylabel('Preu (€)')        
    axs[0, 0].get_xaxis().set_visible(False)

    axs[0, 1].scatter(year, prices)
    axs[0, 1].scatter(moto[YEAR], moto[PRICE], c=MOTO_COLOR, linewidth=MOTO_LW)
    axs[0, 1].set_title('any')
    axs[0, 1].set_ylabel('Preu (€)')
    axs[0, 1].get_xaxis().set_visible(True)

    axs[1, 0].scatter(brand, prices)
    axs[1, 0].scatter(moto[BRAND_ID], moto[PRICE], c=MOTO_COLOR, linewidth=MOTO_LW)
    axs[1, 0].set_title('marca == brand')
    axs[1, 0].set_ylabel('Preu (€)')
    axs[1, 0].get_xaxis().set_visible(False)

    axs[1, 1].scatter(fuel, prices)
    axs[1, 1].scatter(moto[FUEL], moto[PRICE], c=MOTO_COLOR, linewidth=MOTO_LW)
    axs[1, 1].set_title('gasolina')
    axs[1, 1].set_ylabel('Preu (€)')
    axs[1, 1].get_xaxis().set_visible(True)

    fig.suptitle('Comparació multiparamètrica ', fontsize=20)
    plt.show()
    return fig
