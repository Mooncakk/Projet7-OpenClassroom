import json
from decimal import *
from operator import itemgetter

def read_json(filename):
    with open ("liste_actions.json", "r") as file:
        data =  json.load(file)
    return data


stock_list = read_json("stock_list.json")
cost_netprofit_list = [] 

""" Faire une liste de tuples cout/profit_réel"""
for i in range(1, len(stock_list)):
    cost = (stock_list[f'{i}']['cost'])
    profit = (stock_list[f'{i}']['profit'])
    net_profit = cost * (profit/100)
    cost_netprofit_list.append((cost,net_profit))

print(cost_netprofit_list)

""" Classer la liste par ordre décroissant selon les profits réel"""    
cost_netprofit_sorted = sorted(cost_netprofit_list, key=itemgetter(1), reverse=True)
print(cost_netprofit_sorted)

"""Additionner les coûts des actions les plus profitable sans dépasser 500€"""

l = (2,8,4,6,3,5,1,7)
