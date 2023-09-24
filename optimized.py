import pandas as pd
import time


def knapSack(W, wt, val, n):
    # Base Case
    if n == 0 or W == 0:
        return 0

    # If weight of the nth item is
    # more than Knapsack of capacity W,
    # then this item cannot be included
    # in the optimal solution
    if (wt[n - 1] > W):
        return knapSack(W, wt, val, n - 1)

    # return the maximum of two cases:
    # (1) nth item included
    # (2) not included
    else:
        return max(
            val[n - 1] + knapSack(
                W - wt[n - 1], wt, val, n - 1),
            knapSack(W, wt, val, n - 1))


# end of function knapSack


# Driver Code
if __name__ == '__main__':
    # Fichier csv profit = [60, 100, 120]
    start_time = time.time()
    data = pd.read_csv('./Shares.csv', delimiter=';')
    data["Profit"] = data["Cout"] * data["Bénéfice"] / 100

    weight = data.Cout.values

    profit = data.Profit.values
    n = len(profit)
    W = 500

    print(knapSack(W, weight, profit, n))
    print(f'---{time.time() - start_time} secondes---')

# This code is contributed by Nikhil Kumar Singh