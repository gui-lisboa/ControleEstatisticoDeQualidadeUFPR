from statsmodels.tsa.stattools import ccf
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator

def plot_ccf(x, y, lag_range,
             figsize=(12, 5),
             title= "",
             title_fontsize=15,
             xlabel_fontsize=16,
             ylabel_fontsize=16):
    """
    plot cross-correlation between series x and y
    :param x: series that we leads y on the left
    :type x: pd.Series
    :param y: series that we leads x on the right
    :type y: pd.Series
    :param lag_range: range of lag
    :type lag_range: int
    :param figsize: figure size
    :type figsize: tuple
    :param title_fontsize: title font size
    :type title_fontsize: int
    :param xlabel_fontsize: x axis label size
    :type xlabel_fontsize: int
    :param ylabel_fontsize: y axis label size
    :type ylabel_fontsize: int
    """
    if title is None:
        title = "{} & {}".format(x.name, y.name)

    lags = range(-lag_range, lag_range )
    left = ccf(y, x)[:lag_range + 1]
    right = ccf(x, y)[:lag_range]

    left = left[1:][::-1]
    cc = np.concatenate([left, right])

    sigma = 1 / np.sqrt(x.shape[0])
    fig, ax = plt.subplots(figsize=figsize)
    ax.vlines(lags, [0], cc)
    plt.plot(lags, [0] * len(lags), c="black", linewidth=1.0)
    plt.plot(lags, [2 * sigma] * len(lags), '-.', c="blue", linewidth=0.6)
    plt.plot(lags, [-2 * sigma] * len(lags), '-.', c="blue", linewidth=0.6)
    ax.set_xlabel('Lag', fontsize=xlabel_fontsize)
    ax.set_ylabel('cross-correlation', fontsize=ylabel_fontsize)    
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    fig.suptitle(title, fontsize=title_fontsize, fontweight='bold', y=0.93)