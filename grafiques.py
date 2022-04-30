
from math import inf

import matplotlib.pyplot as plt

from config import *


# Reference moto preferences
MOTO_COLOR = 'red'
MOTO_LW = 6


def graficar(wrapper, matrix, moto):
    """
    Plots all the motos in matrix and the reference one

    :param wrapper: data base wrapper
    :param matrix: Nx6 matrix for N motos to show
    :param moto: reference moto
    :return: fig
    """
    prices = matrix[:, PRICE]
    name = matrix[:, NAME]
    year = matrix[:, YEAR]
    brand = matrix[:, BRAND_ID]
    fuel = matrix[:, FUEL]

    fig, axs = plt.subplots(2, 2)

    # Model ID plot
    axs[0, 0].scatter(name, prices)
    axs[0, 0].scatter(moto[NAME], moto[PRICE], c=MOTO_COLOR, linewidth=MOTO_LW)
    axs[0, 0].set_title('Model ID')
    axs[0, 0].set_ylabel('Price €')
    axs[0, 0].grid(True)

    # Year plot
    axs[0, 1].scatter(year, prices)
    axs[0, 1].scatter(moto[YEAR], moto[PRICE], c=MOTO_COLOR, linewidth=MOTO_LW)
    axs[0, 1].set_title('Year')
    axs[0, 1].set_ylabel('Price €')
    axs[0, 1].grid(True)

    # Brand ID plot
    axs[1, 0].scatter(brand, prices)
    axs[1, 0].scatter(moto[BRAND_ID], moto[PRICE], c=MOTO_COLOR, linewidth=MOTO_LW)
    axs[1, 0].set_title('Brand ID')
    axs[1, 0].set_ylabel('Price €')
    axs[1, 0].grid(True)

    # Fuel plot
    axs[1, 1].scatter(fuel, prices)
    axs[1, 1].scatter(moto[FUEL], moto[PRICE], c=MOTO_COLOR, linewidth=MOTO_LW)
    axs[1, 1].set_title('Fuel')
    axs[1, 1].set_ylabel('Price €')
    axs[1, 1].grid(True)

    fig.suptitle('Multiparams comparison', fontsize=20)

    # FIXME: Make it work for all the subplots (and also this one :P)
    # Let the user select a moto from any subplot
    p = plt.ginput(1)[0]
    x = round(p[0])
    y = round(p[1])

    # Subplot where the click was made
    param = YEAR

    # Find closest moto to selection
    err_min = inf
    sel = matrix[0, :]
    for i in range(matrix.shape[0]):
        m = matrix[i, :]
        err = abs(x - m[param]) + abs(y - m[PRICE])

        if err <= err_min:
            err_min = err
            sel = m

    # TODO: Put a label or smth with the closest moto data
    moto_str = wrapper.moto2str(sel)
    print('Selected:\n{}'.format(moto_str))

    box_style = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    axs[0, 1].text(sel[param], sel[PRICE], 'moto_str', {'color': 'red', 'weight': 'heavy', 'size': 20}, bbox=box_style)

    plt.show()

    return fig
