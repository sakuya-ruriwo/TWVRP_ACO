import sys
import numpy as np
import math

def init(bench_file_path):
    #vehicle_num = int(input("Vehicle_num : "))
    
    with open(bench_file_path) as f:
        t = f.readline().split()
        dimension = int(t[2])
        t = f.readline().split()
        capacity = int(t[2])
        f.readline()

        Vloc = np.zeros((dimension + 1 , 2))
        node_demand = np.zeros(dimension + 1)
        tw = np.zeros((dimension + 1 , 2))
        service_time = np.zeros((dimension + 1))


        for i in range (1 , dimension + 1):
            t = f.readline().split()
            Vloc[i][0] = t[1]
            Vloc[i][1] = t[2]
            node_demand[i] = t[3]
            tw[i][0] = t[4]
            tw[i][1] = t[5]
            service_time[i] = t[6]

        f.readline()

    dist = np.zeros((dimension + 1 , dimension + 1))

    for i in range(1 , dimension + 1):
        for j in range(1 , dimension + 1):
            dx = Vloc[i][0] - Vloc[j][0]
            dy = Vloc[i][1] - Vloc[j][1]
            d = (dx ** 2 + dy ** 2) ** 0.5
            dist[i][j] = d

    
    return capacity , dimension , Vloc , node_demand , service_time , tw , dist
        
