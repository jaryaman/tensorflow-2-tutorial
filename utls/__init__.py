import matplotlib.pyplot as plt

def plot(n_rows=1, n_cols=1, fig_size=5):
    """
    Generate a matplotlib plot and axis handle
    Parameters
    -----------------
    n_rows : An int, number of rows for subplotting
    n_cols : An int, number of columns for subplotting
    fig_size : Numeric or array (xfigsize, yfigsize). The size of each axis.
    """
    if isinstance(fig_size,(list, tuple)):
        xfigsize, yfigsize = fig_size
    elif isinstance(fig_size,(int,float)):
        xfigsize = yfigsize = fig_size
    else:
        raise ValueError
    fig, axs = plt.subplots(n_rows, n_cols, figsize=(n_cols*xfigsize, n_rows*yfigsize))
    if n_rows*n_cols > 1:
        axs = axs.ravel()
    return fig, axs
