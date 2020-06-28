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

def read_portfolio_dict_zip(filename):
    portfolio = []
    
    with open(filename) as file:
        rows = csv.reader(file)
        headers = next(rows)

        for rowno, row in enumerate(rows):
            portfolio.append(dict(zip(headers, row)))
            portfolio[rowno]["shares"] = int(portfolio[rowno]["shares"])
            portfolio[rowno]["price"] = float(portfolio[rowno]["price"])

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

def print_report(report, header):
    column_space = 15
    spacer = "+"
    spacer_unit = ""
    seperator = ""

    #Print Header
    print(f"{header[0]:>{column_space}s} {header[1]:>{column_space}s} {header[2]:>{column_space}s} {header[3]:>{column_space}s}")

    #Build Spacer unit
    for i in range(column_space):
        spacer_unit = spacer_unit + spacer
    
    #Build Seperator 
    for column in header:
        seperator = seperator + spacer_unit + " "
    
    print(seperator)
    
    for name, shares, price, change in report:
        pricePrint = "$"+ f"{price:.2f}"
        print(f"{name:>{column_space}s} {shares:>{column_space}d} {pricePrint:>{column_space}s} {change:>{column_space}.2f}")

def make_report(portfolio, prices):
    report = []
    
    #Generate Report
    for row in portfolio:
        try:
            change = float(prices[row["name"]]) - float(row["price"])
            holding = (row["name"], int(row["shares"]), float(prices[row["name"]]), change)
            report.append(holding)
        except:
            print("Error parsing row: ", "\"", row, "\"")

    print_report(report, ("Name", "Shares", "Price", "Change"))

    return report



# Exercise 2.4
