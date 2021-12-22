import matplotlib.pyplot as plt
import numpy as np

def plot(coords , routes , vnum , cost , bname , para):
    for i in range(2 , len(coords)):
        plt.scatter(coords[i][0] , coords[i][1] , c = "black" , s = 5)
    plt.scatter(coords[1][0] , coords[1][1] , c = "red" , s = 25)

    for number , i in enumerate(routes):
        route = [1] + i + [1]
        x = np.empty(0)
        y = np.empty(0)
        for j in route:
            x = np.append(x ,coords[j][0])
            y = np.append(y ,coords[j][1])

        if number == 0:
            plt.plot(x , y , lw = 1)

        else :
            plt.plot(x , y , lw = 0.3)
    
    vnum = str(vnum)
    cost = str(cost)

    info = "Vehicle_num : " + vnum + "\nDistance : " + cost + "\n"
    
    plot_routes = ""
    for i , plot_route in enumerate(routes , 1):
        v = str(i)
        vroute = rebuild_route(plot_route)
        plot_routes = plot_routes + "#" + v + " :  "  + vroute + "\n"

    info = info + plot_routes

    parameter = ""
    for k , v in para.items():
        paraitem = str(k) + " : " + str(v) + " , "
        parameter += paraitem

    title = bname + "\n" + parameter
    plt.title(title)
    plt.legend(title = info , bbox_to_anchor=(1.7, 1) , loc = "upper right" , borderaxespad=0.)
    plt.savefig(bname + ".png", bbox_inches="tight") 

def rebuild_route(Route):
    return_route = ""
    for i in Route:
        customor = str(i)
        return_route = return_route + customor + "-"
    return_route = return_route[:-1]

    return return_route