import sys
import os
import ACO
import ACO_vnum
import plot
from multiprocessing import Pool

try_num = 5

def main(Version , Dir_path):
    file_list = os.listdir(Dir_path)
    os.chdir(Dir_path)
    
    arg = [(Version , file) for file in file_list]
    print(arg)
    p = Pool(6)
    result = p.map(run_and_plot_wrapper , arg)

    print(result)

def run_and_plot_wrapper(args):
    run_and_plot(*args)

    
def run_and_plot(Version , File):
    best_route = []
    best_num = 0
    best_cost = 99999
    best_para = {}

    q0_and_rho = [i / 10 for i in range (0 , 11)]
    
    for alpha in range(0,6):
        for beta in range (0,6):
            for gamma in range(0,6):
                for q0 in q0_and_rho:
                    for rho in q0_and_rho:
                        for i in range(0 , try_num):
                            if Version == "1":
                                vehicle_route , cost , vehicle_num , customer_location , para = ACO.runACO(File , 30 , alpha , beta ,gamma , q0 , rho)
                            elif Version == "2":
                                vehicle_route , cost , vehicle_num , customer_location , para = ACO_vnum.runACO(File , 30 , alpha , beta ,gamma , q0 , rho)

                            if cost < best_cost:
                                best_route = vehicle_route
                                best_num = vehicle_num
                                best_cost = cost
                                best_para = para
                        print(File , "alpha : ",alpha,"beta : ",beta,"gamma : ",gamma,"q0 : ",q0,"rho : ",rho )
                            
                    
                    #print("---------" , i+1 , "/ 10" ,"---------")
       
    print(best_route , "\nvehicle_num : " ,best_num , "\ndistance : " , best_cost)
    file_name = File.replace(".txt" , " ")
    plot.plot(customer_location , best_route , best_num , best_cost ,  file_name , best_para)
    return file_name

if __name__ == '__main__' : 
    ACO_ver = input("1 : normal\n2 : vnum\n")
    dir_path = sys.argv[1]
    main(ACO_ver , dir_path)
    