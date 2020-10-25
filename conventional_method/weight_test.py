import sys
import matplotlib.pyplot as plt
import numpy as np
import math
log = np.loadtxt( 'ave_dist_collision_each_weight.csv',delimiter = ',')

# Create some mock data
t = np.arange(4, 6.3, 0.4)

fig, ax1 = plt.subplots()

color = 'r'
ax1.set_xlabel('Separation/Avoidance weight',size = 23)
ax1.set_ylabel('Number of crashed drones',size = 23, color=color)
ax1.plot(t, log[:,1],'-^', color=color, label='Number of crashed drones', markersize=10)
ax1.tick_params(axis="both", labelsize=20)
ax1.set_xticks(np.arange(4, 6.1, 0.4))
ax1.set_xlim([4, 6])
ax1.set_ylim([0, 40])
ax1.grid(which='major', axis = 'y')
ax1.legend(prop={"size":20}, loc='lower right')
ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'b'
ax2.set_ylabel('Average distance',size = 23, color=color)  # we already handled the x-label with ax1
ax2.plot(t, log[:,0], '-v',color=color,label='Average distance', markersize=10)
ax2.tick_params(axis="both", labelsize=20)
ax2.set_ylim([94, 102])
fig.tight_layout()  # otherwise the right y-label is slightly clipped
ax2.legend(prop={"size":20}, loc='center right')
plt.show()