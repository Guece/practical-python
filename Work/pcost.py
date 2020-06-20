# pcost.py
import sys

def ohne_csv_portfolio_cost(filename):
    total_cost = 0.0

    costs = []
    entries = 0
    with open(filename, "rt") as file:
        headers = next(file)

        for line in file:
            row = line.split(",")
            
            try:            
                name = row[0]
                share_amount= int(row[1])
                cost_per_share = float((row[2])[:-1])
            except ValueError:
                print("Couldn't parse", line)
                continue

            costs.append(share_amount * cost_per_share)

            entries = entries + 1

    for i in costs:
        total_cost = total_cost + i

    return total_cost

def mit_csv_portfolio_cost(filename):
    import csv

    total_cost = 0.0
    with open(filename) as file:
        rows = csv.reader(file)
        headers = next(rows)

        for row in rows:
            try:
                share_amount = int(row[1])
                cost_per_share = float(row[2])
                
                total_cost = total_cost + (share_amount * cost_per_share)
            except ValueError:
                print ("Couldn't parse", row)
                continue
    return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = "Data/portfolio.csv"
cost = mit_csv_portfolio_cost(filename)
print("Total cost:", cost)
cost = ohne_csv_portfolio_cost(filename)
print("Total cost:", cost)
# Exercise 1.27
