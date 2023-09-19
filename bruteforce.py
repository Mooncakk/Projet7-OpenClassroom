import pandas as pd
from itertools import combinations
import time

def shares(data='./Shares.csv'):
    '''Lis le fichier csv et créé un tuples contenant les infos des actions, les prix et le bénéfice apres 2 ans''' 

    data = pd.read_csv(data, delimiter = ';')
    shares_list = []

    for row in data.itertuples():
        share = row[1]
        price = row[2]
        efficiency = row[3]
        profit = price * efficiency/100
        share_infos = share, price, profit
        shares_list.append(share_infos)
               
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
            combination_profit += profit[2]
        combination_profit_list.append(combination_profit)

    return combination_profit_list


def combination_infos(combination_list, combination_price, combination_profit):
    '''Créé une liste avec les combinations, le prix et le bénéfice de chacune d'elle'''

    combination_infos = []

    for combination, price, profit in zip(combination_list, combination_price, combination_profit):

        combination_infos.append((combination, price, profit))
    
    return combination_infos


        
def best_result(combination_infos):
    '''Récupère la meilleure combinaison en terme de bébéfice sans dépenser plus de 500€'''

    price = 0
    best_profit = 0
    
    for combination in combination_infos:
        if combination[1] <= 500 and combination[2] > best_profit:
            price = combination[1]
            best_profit = combination[2]
            best_combination = combination

    best_shares = [share[0] for share in best_combination[0]]

    return best_shares, price, best_profit

def main():

    share_list = shares()
    combination = combination_list(share_list)
    price = combination_price(combination)
    profit = combination_profit(combination)
    infos = combination_infos(combination, price, profit)
    best_combination, best_combination_price, best_combination_profit = best_result(infos)

    print(f"Le meilleur investissement est la combinaison d'actions : {best_combination}")
    print(f"Avec un bénéfice de : {best_combination_profit}€ après 2 ans")
    print(f"Pour un coût d'achat total de: {best_combination_price}€")


if __name__ == '__main__':
    start_time = time.time()
    main()
    print(f'---{time.time()-start_time} secondes---')