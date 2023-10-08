import pandas as pd
from itertools import combinations
import time

def shares(data='./Shares.csv'):
    '''Lis le fichier csv et créé une liste contenant les infos des actions, les prix, les bénéfices apres 2 ans'''

    data = pd.read_csv(data, delimiter = ';')
    data["Profit"] = data["Cout"] * data["Bénéfice"] / 100
    shares_list = data.values

    return shares_list

def combination_list(shares_list):
    '''Compare toutes les combinantions possible entre les actions et enregistre chaque combinaison dans une liste'''

    combination_list = []

    for i in range(1, len(shares_list)+1):
        for combination in combinations(shares_list, i):
            combination_list.append(combination)

    return combination_list


def combination_price(combination_list):
    '''Calcul le prix de chaque combinaison'''

    combination_price_list = []

    for combination in combination_list:
        combination_price = 0       
        for price in combination:    
            combination_price += price[1]
        combination_price_list.append(combination_price)

    return combination_price_list


def combination_profit(combination_list):
    '''Calcul le bénéfice de chaque combinaison'''

    combination_profit_list = []

    for combination in combination_list:
        combination_profit = 0        
        for profit in combination:
            combination_profit += profit[3]
        combination_profit_list.append(combination_profit)

    return combination_profit_list

def best_result(combination_list, combination_price, combination_profit):
    '''Récupère la meilleure combinaison en terme de bébéfice sans dépenser plus de 500€'''

    price = 0
    best_profit = 0
    
    for i, combination in enumerate(combination_list):

        if combination_price[i] <= 500 and combination_profit[i] > best_profit:
            best_combination = combination
            price = combination_price[i]
            best_profit = combination_profit[i]

    best_shares = [share[0] for share in best_combination]


    return best_shares, price, round(best_profit,2)

if __name__ == '__main__':
    start_time = time.time()

    share_list = shares()
    combination = combination_list(share_list)
    price = combination_price(combination)
    profit = combination_profit(combination)
    best_combination, best_combination_price, best_combination_profit = best_result(combination, price, profit)
    best_combination = ', '.join(best_combination)

    print(f"Le meilleur investissement est la combinaison d'actions : {best_combination}")
    print(f"Avec un bénéfice de : {best_combination_profit}€ après 2 ans")
    print(f"Pour un coût d'achat total de: {best_combination_price}€")
    print(f'---{time.time()-start_time} secondes---')