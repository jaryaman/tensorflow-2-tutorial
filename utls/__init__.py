from IPython import get_ipython
import matplotlib.pyplot as plt
import tensorflow as tf
import tensorflow_hub as hub


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


def auto_reload():
    """
    Let python functions be updated whilst inside an iPython/Jupyter session
    """
    ipython = get_ipython()
    ipython.magic("reload_ext autoreload")
    ipython.magic("autoreload 2")


def tf_status():
    print("Version: ", tf.__version__)
    print("Eager mode: ", tf.executing_eagerly())
    print("Hub version: ", hub.__version__)
    print("GPU is", "available" if tf.config.experimental.list_physical_devices("GPU") else "NOT AVAILABLE")
