import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# The function creates a bivariate colormap from the combination of cmap1 and cmap2
# Edited from https://gist.github.com/wolfiex/64d2faa495f8f0e1b1a68cdbdf3817f1#file-bivariate-py

def biv_map(x,y,cmap1 = plt.cm.Blues, cmap2 = plt.cm.Reds, preset = False):
    xmn = x.min()
    ymn = y.min()
    xmx = x.max()
    ymx = y.max()

    # Rescale values to fit into colormap range (0->255)
    X_plot = np.array(255*(x-xmn)/(xmx-xmn), dtype=np.int)
    Y_plot = np.array(255*(y-ymn)/(ymx-ymn), dtype=np.int)

    X_color = cmap1(X_plot)
    Y_color = cmap2(Y_plot)

    # Color for each point
    Z_color = np.sum([X_color, Y_color], axis=0)/2.0

    return Z_color
