import sys
import matplotlib.pyplot as plt
import numpy as np
import math
if len(sys.argv)>1:
    log = np.loadtxt( 'proposed_method/proposed_method.csv',delimiter = ',', max_rows=201)
    log1= np.loadtxt( 'conventional_method/conventional_method.csv',delimiter = ',', max_rows=201)
    x = [i for i in range(len(log))]
    x1 = [i for i in range(len(log1))]
    fig = plt.figure()

# #########################################################################################
    ax = fig.add_subplot(1, 1, 1)
    ax.set_yticks(np.arange(-1, 10, 1))
    ax.set_xticks(np.arange(0, 200, 25), minor=True)
    ax.grid(which='major', axis = 'y')
    ax.tick_params(axis="both", labelsize=20)

    plt.ylabel( 'Number of crashed drones',size = 26)
    plt.xlabel( 'Iteration' ,size = 26)
    plt.plot(x, log[:,1],'b^', label = 'Proposed Method', markersize=12)
    plt.axis([0, 200, -2, 5] )#size = 26)
    plt.legend(prop={"size":20})

    plt.show()
else:
    log = np.loadtxt( 'proposed_method/proposed_method_no_ob.csv',delimiter = ',')
    log1= np.loadtxt( 'conventional_method/conventional_method_no_ob.csv',delimiter = ',')
    n = min(len(log),len(log1))
    diff = [(log[i,0]- log1[i,0]) for i in range(n)]
    x = [i for i in range(len(log))]
    x1 = [i for i in range(len(log1))]
    x2 = [i for i in range(n)]
    fig = plt.figure()
    ax = fig.add_subplot(1, 2, 1)
    ax.grid(which='both')
    plt.ylabel( 'Average Distance (no obstacles)' )
    plt.xlabel( 'Simulation' )
    plt.plot(x, log[:,0],'y', label='dynamic')
    plt.plot(x1, log1[:,0],'r', label = 'fixed')
    plt.axis([0, 80, 0, 200])
    plt.legend()

    ax = fig.add_subplot(1, 2, 2)
    ax.grid(which='both')
    plt.ylabel( 'Average Distance Difference (no obstacles)' )
    plt.xlabel( 'Simulation' )
    plt.plot( x2, diff, label='difference')
    plt.axis([0, 80, -100, 100])
    plt.legend()
    plt.show()
