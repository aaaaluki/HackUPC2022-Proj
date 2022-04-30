import matplotlib.pyplot as plt

from config import *


# Reference moto preferences
MOTO_COLOR = 'red'
MOTO_LW = 6


def graficar(matrix, moto):
    """
    Plots all the motos in matrix and the reference one

    :param matrix: Nx6 matrix for N motos to show
    :param moto: reference moto
    :return: fig
    """
    prices = matrix[:,PRICE]
    name = matrix[:,NAME]
    year = matrix[:,YEAR]
    brand = matrix[:,BRAND_ID]
    fuel = matrix[:,FUEL]

    fig, axs = plt.subplots(2, 2, constrained_layout=True)

    # Model ID plot
    axs[0, 0].scatter(name, prices)
    axs[0, 0].scatter(moto[NAME], moto[PRICE], c=MOTO_COLOR, linewidth=MOTO_LW)
    axs[0, 0].set_title('Model ID')
    axs[0, 0].set_ylabel('Price €')
    axs[0, 0].get_xaxis().set_visible(False)

    # Year plot
    axs[0, 1].scatter(year, prices)
    axs[0, 1].scatter(moto[YEAR], moto[PRICE], c=MOTO_COLOR, linewidth=MOTO_LW)
    axs[0, 1].set_title('Year')
    axs[0, 1].set_ylabel('Price €')
    axs[0, 1].get_xaxis().set_visible(True)

    # Brand ID plot
    axs[1, 0].scatter(brand, prices)
    axs[1, 0].scatter(moto[BRAND_ID], moto[PRICE], c=MOTO_COLOR, linewidth=MOTO_LW)
    axs[1, 0].set_title('Brand ID')
    axs[1, 0].set_ylabel('Price €')
    axs[1, 0].get_xaxis().set_visible(False)

    # Fuel plot
    axs[1, 1].scatter(fuel, prices)
    axs[1, 1].scatter(moto[FUEL], moto[PRICE], c=MOTO_COLOR, linewidth=MOTO_LW)
    axs[1, 1].set_title('Fuel')
    axs[1, 1].set_ylabel('Price €')
    axs[1, 1].get_xaxis().set_visible(True)

    fig.suptitle('Multiparams comparison', fontsize=20)
    plt.show()
    return fig
