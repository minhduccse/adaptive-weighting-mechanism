import sys
import matplotlib.pyplot as plt
import numpy as np
import math
if len(sys.argv)>1:
    log = np.loadtxt('proposed_method/proposed_method.csv',delimiter = ',', max_rows=201)
    log1= np.loadtxt('conventional_method/conventional_method.csv',delimiter = ',', max_rows=201)
    x = [i for i in range(len(log))]
    x1 = [i for i in range(len(log1))]
    fig = plt.figure()

    #average distance for each
    ax = fig.add_subplot(1, 1, 1)
    major_yticks = np.arange(0, 201, 20)
    minor_yticks = np.arange(0, 201, 5)
    minor_ticks = np.arange(0, 201, 25)
    ax.set_xticks(minor_ticks)
    ax.set_yticks(major_yticks)
    ax.set_yticks(minor_yticks, minor=True)
    ax.tick_params(axis="both", labelsize=20)
    # ax.set_xticklabels([])

    ax.grid(which='major', axis = 'y')
    plt.ylabel( 'Flock compactness (unit)', size = 26)
    plt.xlabel( 'Iteration', size = 26)
    plt.plot( x, log[:,0], 'b-',label='Proposed Method')
    plt.plot( x1, log1[:,0], 'r--', label = 'Conventional Method')
    plt.axis([0, 200, 60, 160])
    plt.legend(prop={"size":20}, frameon=False, loc='upper right')

#######################################################################################
    # ax = fig.add_subplot(1, 1, 1) #1,3,2
    # ax.set_yticks(np.arange(-1, 10, 1))
    # ax.set_xticks(np.arange(0, 200, 25), minor=True)
    # ax.grid(which='major', axis = 'y')
    # ax.tick_params(axis="both", labelsize=20)
    # # ax.set_xticklabels([])


    # plt.ylabel( 'Number of crashed drones',size = 26 )
    # plt.xlabel( 'Iteration' ,size = 26)
    # plt.plot(x1,log1[:,1],'rv', label = 'Conventional Method', markersize=12)
    # plt.axis([0, 200, -2, 5])
    # plt.legend(prop={"size":20})


# ###########################################################################################
    # ax = fig.add_subplot(1, 1, 1)
    # ax.set_yticks(np.arange(-1, 10, 1))
    # ax.set_xticks(np.arange(0, 200, 25), minor=True)
    # ax.grid(which='major', axis = 'y')
    # ax.tick_params(axis="both", labelsize=20)
    # # ax.set_xticklabels([])


    # plt.ylabel( 'Number of crashed drones',size = 26)
    # plt.xlabel( 'Iteration' ,size = 26)
    # plt.plot(x, log[:,1],'b^', label = 'Proposed Method', markersize=12)
    # plt.axis([0, 200, -2, 5]) #, size = 26)
    # plt.legend(prop={"size":20})

#     avs = sum(log[0:100,0])
#     avs1 = sum(log1[0:100,0])
#     print(avs/len(log[0:100,0]),avs1/len(log1[0:100,0]),avs-avs1)

    plt.show()

else:
    log = np.loadtxt( 'proposed_method/proposed_method_no_ob.csv', delimiter = ',')
    log1= np.loadtxt( 'conventional_method/conventional_method_no_ob.csv', delimiter = ',')
    n = min(len(log),len(log1))
    diff = [(log[i,0]- log1[i,0]) for i in range(n)]
    x = [i for i in range(len(log))]
    x1 = [i for i in range(len(log1))]
    for i in range(0,201):
        log1[i,0] = log1[i,0]+1
    x2 = [i for i in range(n)]
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    # major_ticks = np.arange(0, 201, 20)
    # minor_ticks = np.arange(0, 201, 25)
    # ax.set_xticks(minor_ticks)
    # ax.set_yticks(major_ticks)
    # ax.set_yticks(minor_ticks, minor=True)
    # #ax.grid(which='both')
    major_yticks = np.arange(0, 201, 10)
    minor_yticks = np.arange(0, 201, 5)
    minor_ticks = np.arange(0, 201, 25)
    ax.set_xticks(minor_ticks)
    ax.set_yticks(major_yticks)
    ax.set_yticks(minor_yticks, minor=True)
    ax.tick_params(axis="both", labelsize=20)
    # ax.set_xticklabels([])

    ax.grid(which='major', axis = 'y')
    plt.ylabel( 'Flock compactness (unit)' , size = 26)
    plt.xlabel( 'Iteration' , size = 26)
    plt.plot(x, log[:,0],'b', label='Proposed Method')
    plt.plot(x1, log1[:,0],'r--', label = 'Conventional Method')
    plt.axis([0, 200, 60, 110])
    plt.legend(prop={"size":20}, frameon=False, loc='upper right')



    # ax = fig.add_subplot(1, 2, 2)
    # # Major ticks every 20, minor ticks every 5
    # # major_ticks = np.arange(-100, 201, 20)
    # # minor_ticks = np.arange(-100, 201,5)
    # # ax.set_xticks(minor_ticks)
    # # ax.set_yticks(major_ticks)
    # # ax.set_yticks(minor_ticks, minor=True)
    # ax.grid(which='both')
    # plt.ylabel( 'Average Distance Difference (no obstacles)' )
    # plt.xlabel( 'Simulation' )
    # plt.plot( x2, diff, label='difference')
    # plt.axis([0, 80, -100, 100])
    # plt.legend()

    avs = sum(log[0:200,0])
    avs1 = sum(log1[0:200,0])
    print(avs/len(log[0:200,0]),avs1/len(log1[0:200,0]),avs-avs1)

    plt.show()
