import json
from decimal import *
from operator import itemgetter
from itertools import accumulate

def read_json(filename):
    with open ("liste_actions.json", "r") as file:
        data =  json.load(file)
    return data


share_list = read_json("stock_list.json")
cost_netprofit_list = [] 

""" Faire une liste de tuples action/cout/profit_réel"""
for i in range(1, len(share_list)+1):
    cost = (share_list[f'{i}']['cost'])
    profit = (share_list[f'{i}']['profit'])
    net_profit = cost * (profit/100)
    cost_netprofit_list.append((i, cost,net_profit))

#print(cost_netprofit_list)

""" Classer la liste par ordre décroissant selon les profits réel"""    
cost_netprofit_sorted = sorted(cost_netprofit_list, key=itemgetter(2), reverse=True)
#print(cost_netprofit_sorted)
swap = True
while swap:
    swap = False
    for i in range(0,len(cost_netprofit_list)-1):
        if cost_netprofit_list[i+1][2] > cost_netprofit_list[i][2]:
            cost_netprofit_list[i], cost_netprofit_list[i+1] = cost_netprofit_list[i+1], cost_netprofit_list[i]
            swap=True

"""Additionner les coûts des actions les plus profitable sans dépasser 500€"""

stockscost = 0
"""while stockscost < 501:

    a = list(accumulate(cost_netprofit_sorted[2]))

    for i in cost_netprofit_sorted:
        stockscost += i[2]
        #print(stockscost)"""




l = (2,8,4,6,3,5,1,7)
