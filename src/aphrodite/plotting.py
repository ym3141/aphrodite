import seaborn as sns
import numpy as np

import matplotlib.pyplot as plt

__all__ = ["bar_point_plot", "closer_strip_plot"]


def bar_point_plot(
    data=None, x=None, y=None, hue=None, order=None, hue_order=None, estimator='mean', errorbar=None, dodge=True,
    orient='v', color=None, palette='Set2', saturation=0.75, fill=True, hue_norm=None, width=0.8, gap=0, dot_size=5,
    log_scale=False, native_scale=False, formatter=None, legend='auto', capsize=0, err_kws=None, despline=True,
    ax=None, **kwargs
):
    if hue is None:
        hue = x

    shared = dict(
        data=data, x=x, y=y, hue=hue, order=order, hue_order=hue_order,
        dodge=dodge, orient=orient, palette=palette, hue_norm=hue_norm,
        log_scale=log_scale, native_scale=native_scale, formatter=formatter,
    )
    bar_options = {"edgecolor": "black", "linewidth": 1, **kwargs}

    ax = sns.barplot(
        **shared,
        estimator=estimator, errorbar=errorbar, color=color, saturation=saturation,
        fill=fill, width=width, gap=gap, legend=legend, capsize=capsize,
        err_kws=err_kws, ax=ax, **bar_options
    )

    if hue is None:
        dot_color = 'gray' if color is None else color
    else:
        dot_color = None  # Let seaborn handle the color based on hue

    sns.stripplot(
        **shared,
        color=dot_color, alpha=0.7, size=dot_size,
        edgecolor=bar_options["edgecolor"], linewidth=bar_options["linewidth"],
        legend=False, ax=ax
    )

    if despline:
        sns.despine(ax=ax)

    return ax


def closer_strip_plot(hue_order, *args, dodge=0.5, **kwargs):
    ax = kwargs.pop("ax", None)
    if ax is None:
        ax = plt.gca()

    # shrink_in_dodge = kwargs.pop("dodge", 0.5)
    n_hue = len(hue_order)
    shrink = (
        float(dodge) / (0.8 * (n_hue - 1) / n_hue)
        if n_hue > 1 else 1.0
    )

    # Track existing collections so only this stripplot is adjusted.
    n_existing = len(ax.collections)

    sns.stripplot(*args, ax=ax, hue_order=hue_order, dodge=True, **kwargs)

    for collection in ax.collections[n_existing:]:
        offsets = collection.get_offsets().copy()
        if len(offsets) == 0:
            continue

        centers = np.round(offsets[:, 0])
        offsets[:, 0] = centers + shrink * (offsets[:, 0] - centers)
        collection.set_offsets(offsets)

    return ax

