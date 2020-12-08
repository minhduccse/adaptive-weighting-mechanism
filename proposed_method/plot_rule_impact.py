import numpy as np
import pandas as pd
from itertools import cycle, islice

import matplotlib.pyplot as plt
np.random.seed(2015)

y = np.random.randint(5, 50, (10,3))

log= np.loadtxt('proposed_rule_impact.csv',delimiter = ',')

df = pd.DataFrame({'Avoidance':log[:,0],'Separation':log[:,1],'Alignment':log[:,2],'Cohesion':log[:,3],'Migration':log[:,4]})

df = df.divide(df.sum(axis=1), axis=0)

col = list(islice(cycle(['green', 'orange', 'black', 'yellow', 'purple']), None, len(df)))

ax = df.plot.area(linewidth=0,stacked=True, y=['Migration', 'Cohesion', 'Alignment', 'Separation', 'Avoidance'], color=col)

ax.set_ylabel('Rule impact\'s ratio', size = 26)
ax.set_xlabel('Steps', size = 26)
ax.tick_params(axis="both", labelsize=20)
ax.margins(0, 0) # Set margins to avoid "whitespace"
plt.legend(prop={"size":20}, loc='lower right')
plt.ylim([0,1])
plt.show()
