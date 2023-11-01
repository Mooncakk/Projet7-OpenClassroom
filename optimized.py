import pandas as pd
import time

def stock_portfolio(price, profit, money, n):

    if n == 0 or money == 0:
        return 0
    if t[n][money] != -1:
        return round((t[n][money]), 2)


    if price[n - 1] <= money:
        t[n][money] = max(
            profit[n - 1] + stock_portfolio(
                price, profit, money - price[n - 1], n - 1),
            stock_portfolio(price, profit, money, n - 1))
        return round((t[n][money]), 2)
    elif price[n - 1] > money:
        t[n][money] = stock_portfolio(price, profit, money, n - 1)
        return round((t[n][money]), 2)


if __name__ == '__main__':
    start_time = time.time()
    data = pd.read_csv('./Shares.csv', delimiter=';')
    data['Net_Profit'] = data.Cout.values * data.Bénéfice.values / 100
    #print(data)
    profit = data.Net_Profit.values
    price = data.Cout.values
    share = data.Actions.values
    sh_pr = []
    for shar, prof in zip(share, profit):
        sh_pr.append((shar, prof))

    money = 500
    n = len(profit)
    print(sh_pr)

    t = [[-1 for i in range(money + 1)] for j in range(n + 1)]
    final_profit = stock_portfolio(price, profit, money, n)

    print(f"Le meilleur investissement est la combinaison d'actions : ? Actions ? ")
    print(f"Avec un bénéfice de : {final_profit}€ après 2 ans")
    print(f"Pour un coût d'achat total de: ? Price ?€")
    print(f'---{time.time() - start_time} secondes---')

'''Extraire les actions choisi par le script'''
'''Extraire le montant utilisé'''