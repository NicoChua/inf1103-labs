inventory = 0
failedEntry = 0

menuOpen = True
while menuOpen == True:
    if inventory > 500:
        print("Inventory Exceeded 500 units")
        break
    stockQty = input("Enter Stock Quantity: ")
    if stockQty == "Quit":
        menuOpen = False
    elif stockQty.isdigit() == True:
        inventory += int(stockQty)
    else:
        print("Please input a number")
        failedEntry += 1
