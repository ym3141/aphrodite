import seaborn as sns
import numpy as np
from matplotlib.colors import ListedColormap

prism_pallete1 = sns.color_palette(['#3BA99A', '#C93963', '#7E94C4', '#74A13C', '#FC584F'])

def clipped_cmap(palette=None, clip_lower=.1, clip_upper=None):
    if not (clip_lower >= 0 and clip_lower < 0.5):
        raise ValueError(f"clip_lower must satisfy 0 <= clip_lower < 0.5; got {clip_lower!r}.")
    if clip_upper is None:
        clip_upper = 1 - .1
    elif not (clip_upper > 0.5 and clip_upper < 1.):
        raise ValueError(f"clip_upper must satisfy 0.5 < clip_upper < 1; got {clip_upper!r}.")

    sns_palette = sns.color_palette(palette, as_cmap=True).copy()
    color_list = sns_palette(np.linspace(clip_lower, clip_upper, 256))
    return ListedColormap(color_list)
