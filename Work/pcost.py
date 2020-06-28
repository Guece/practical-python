# pcost.py
import sys

def ohne_csv_portfolio_cost(filename):
    total_cost = 0.0

    costs = []
    entries = 0
    with open(filename, "rt") as file:
        headers = next(file)

        for lineno, line in enumerate(file, start=1):
            row = line.split(",")
            
            try:            
                name = row[0]
                share_amount= int(row[1])
                cost_per_share = float((row[2])[:-1])
            except ValueError:
                print(f"Couldn't parse line {lineno}: {line}")
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

        for lineno, row in enumerate(rows, start=1):
            try:
                share_amount = int(row[1])
                cost_per_share = float(row[2])
                
                total_cost = total_cost + (share_amount * cost_per_share)
            except ValueError:
                print (f"Couldn't parse line {lineno}: {row}")
                continue
    return total_cost

def csv_zip_portfolio_cost(filename):
    import csv

    total_cost = 0.0

    with open(filename) as file:
        rows = csv.reader(file)
        headers = next(rows)
        
        for lineno, line in enumerate(rows, start=1):
            record = dict(zip(headers, line))
            try:
                share_amount = int(record["shares"])
                price = float(record["price"])
                total_cost += share_amount * price
            except:
                print(f"Couldn't parse line {lineno}: {line}")
                continue
    
    return total_cost 

#Falls man andere File verwenden will
if len(sys.argv) == 3:
    filename = sys.argv[2]
else:
    filename = "Data/portfolio.csv"

#Gemacht, damit man die anderen "schlechteren" funktionen aus vorherigeren Aufgaben
#auch noch nutzen kann
if sys.argv[1] != "zip":
    cost = mit_csv_portfolio_cost(filename)
    print("Total cost:", cost)
    cost = ohne_csv_portfolio_cost(filename)
    print("Total cost:", cost)
else:
    cost = csv_zip_portfolio_cost(filename)
    print(f"Total cost: {cost}")
# Exercise 1.27
