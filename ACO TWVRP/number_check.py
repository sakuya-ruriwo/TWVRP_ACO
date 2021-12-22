import sys
import os
import ACO_vnum
try_num = 5

def run(file):
    for ant_num in range(25,101,25):
        best_route = []
        best_num = 0
        best_cost = 99999
        for i in range(0 , try_num):
            vehicle_route , cost , vehicle_num , customer_location , para = ACO_vnum.runACO(file , ant_num , 1 , 3 ,2 , 0.2 , 0.9)
            if cost < best_cost:
                best_route = vehicle_route
                best_num = vehicle_num
                best_cost = cost
                                   
        print("ant_num : " , ant_num , "\nvehicle_num : " ,best_num , "\ndistance : " , best_cost)

if __name__ == '__main__' : 
    file_path = sys.argv[1]
    run(file_path)
    