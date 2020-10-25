import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
np.random.seed(2015)

y = np.random.randint(5, 50, (10,3))

log= np.loadtxt( 'proposed_method_breakdown.csv',delimiter = ',')

df = pd.DataFrame({'avoidance':log[:,0],'separation':log[:,1],'alignment':log[:,2],'cohesion':log[:,3],'migration':log[:,4]})

df = df.divide(df.sum(axis=1), axis=0)
ax = df.plot.area(linewidth = 0 ,stacked=True, y = ['migration', 'cohesion', 'alignment', 'separation', 'avoidance'])

ax.set_ylabel('Rule impact\'s ratio', size = 26)
ax.set_xlabel('Steps', size = 26)
ax.tick_params(axis="both", labelsize=20)
ax.margins(0, 0) # Set margins to avoid "whitespace"
plt.legend(prop={"size":20})
plt.ylim([0,1])
plt.show()
