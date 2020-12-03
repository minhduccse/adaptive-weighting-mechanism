# Adaptive Weighting Mechanism for Reynolds Rules-based Flocking Control Scheme
  
## 1. Prerequisites

Run the simulation on ***Ubuntu 18.04***

**Install Python3 via pip**

    $ sudo apt-get update
    $ sudo apt-get install python3-pip

**Install pygame**

    $ pip3 install -U pygame --user

## 2. Instruction

**Run the conventional method with obstacles**

    $ cd conventional_method
    $ python3 flock.py 1

**Run the proposed method with obstacles**

    $ cd proposed_method
    $ python3 flock.py 1

**Run without obstacles**

    $ python3 flock.py

## 3. Plot graphs

**Plot flock compactness figures**

 Scenarios with obstacles:

    $ python3 plot.py

 Scenarios without obstacles:

     $ python3 plot.py 1


**Plot rule impact figures**

Conventional method:

    $ cd conventional_method
    $ python3 plot_rule_impact.py

Proposed method:

    $ cd proposed_method
    $ python3 plot_rule_impact.py


**Usage**

 - Right click to add obstacles
