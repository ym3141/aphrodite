import matplotlib.pyplot as plt
import numpy as np
from aphrodite import bar_point_plot

data = {
    "group": ["A", "A", "A", "B", "B"] * 3,
    "sample": ["control", "test1", "test2"] * 5,
    "value": [.3, 4, 4, .4, 5, 1, .3, 5, 8, .6, 4, 2, .8, 10, 9] + np.random.random(15) + 1,
}

ax = bar_point_plot(data=data, x="sample", y="value", hue="group", legend='brief')
ax.set(xlabel="sample", ylabel="Value")
plt.show()
