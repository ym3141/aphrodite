import seaborn as sns
from .plotting import *
from .util import *

sns.set_theme("talk", style="ticks", palette='Set2', 
              rc={"figure.dpi": 150, "font.family": "Arial"})
sns.despine()

