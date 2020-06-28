import csv

def read_portfolio_tuple(filename):
    portfolio = []
        
    with open(filename) as file:
        rows = csv.reader(file)
        header = next(rows)

        for row in rows:
            try:
                holding = (row[0], int(row[1]), float(row[2]))
                portfolio.append(holding) 
            except ValueError:
                print("Error parsing row: ","\"" ,row,"\"")
                continue
    
    return portfolio 

def read_portfolio_dict(filename):
    portfolio = []

    with open(filename) as file:
         rows = csv.reader(file)
         header = next(rows)

         for row in rows:
             try:
                 holding = {"name":row[0], "shares":int(row[1]), "price":float(row[2])}
                 portfolio.append(holding)
             except ValueError:
                 print("Error parsing row: ","\"" ,row,"\"")
                 continue

    return portfolio

def read_prices(filename):
    prices = {}

    with open(filename) as file:
        rows = csv.reader(file)
        
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except:
                print("Error parsing row: ", "\"", row, "\"")
                continue
    
    return prices

def compute_gain(portfolioFile, priceFile):
    portfolio = read_portfolio_dict(portfolioFile)
    currentPrices = read_prices(priceFile)
    
    buyPrice = 0.0
    currentValue = 0.0
    gain = 0.0

    for record in portfolio:
        try:
            currentValue = currentValue + record["shares"] * currentPrices[record["name"]] 
            buyPrice = buyPrice + record["shares"] * record["price"]
        except:
            print("Error for record: \"", record, "\"")
            continue 

    gain = currentValue - buyPrice
    
    infoString = ""
    
    if gain >= 0:
        infoString = f"Es wurde ein Gewinn von ${gain:0.2f} erzielt!"
    else:
        infoString = f"Es wurde ein Verlust von ${gain:0.2f} erzielt!"

    print(infoString)
# Exercise 2.4
