import seaborn as sns
import numpy as np

from matplotlib.colors import to_rgba
import matplotlib.pyplot as plt

def y_to_perc(ax):
    """Convert y-axis to percentage format."""
    from matplotlib.ticker import FuncFormatter
    ax.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.0%}'.format(y)))

def rotate_xtick_labels(ax, angle=45, ha='right'):
    """Rotate x-axis labels."""
    positions = ax.get_xticks()
    labels = ax.get_xticklabels()
    ax.set_xticks(positions, labels=labels, rotation=angle, ha=ha)