# Global Constants
MAX_CAPACITY = 500
TAX_RATE = 0.1
FAILED_ENTRY = 0
INVENTORY_FILE = "inventory.txt"

# Gets and validates user input
def get_valid_input():
    global FAILED_ENTRY
    user_input = input("Enter Stock Quantity: ")
    if user_input == "quit":
        return "quit"
    elif user_input.isdigit() != True:
        print("Please input a number")
        FAILED_ENTRY += 1
        return None
    return user_input

def process_delivery(current_total, new_value):
    new_total = current_total + int(new_value)
    return new_total

def calculate_tax(amount):
    global TAX_RATE
    tax = float(amount) * TAX_RATE
    return tax

def generate_report(total_units, failed_entries):
    print("Total Deliveries Processed: " + str(total_units))
    print("Number of Failed/Rejected Entries: " + str(failed_entries))

# Loads Inventory from inventory.txt
def load_inventory():
    inventory = 0
    transaction_history = []
        
    with open(INVENTORY_FILE, "r") as file:
        firstLine = file.readline()
        if firstLine:
            inventory = int(firstLine)
        transaction_history = file.readlines()
    return inventory, transaction_history

# Stores inventory and transaction history into inventory.txt
def save_inventory(inventory, transaction_history):
    with open("inventory.txt", "w") as file:
        file.write(str(inventory) + "\n")
        file.writelines(transaction_history)

def main():
    # Variables
    inventory = 0
    tax_amount = 0
    exit_program = False
    global MAX_CAPACITY
    transaction_history = []

    # Load Inventory
    inventory, transaction_history = load_inventory()

    # Shows Current Inventory and Transaction History
    print("Inventory: " + str(inventory))
    for line in transaction_history[1:]:
        print("Transaction History: " + line.strip())

    # Main Program to get user input
    while not exit_program:
        stockQty = get_valid_input()
        if stockQty == "quit":
            exit_program = True
        elif stockQty == None:
            continue
        else:
            if inventory >= MAX_CAPACITY:
                break
            inventory = process_delivery(inventory, stockQty)
            tax_amount += calculate_tax(stockQty)
            transaction_history.append(f"\n{stockQty}")

    # Final Output
    generate_report(inventory, FAILED_ENTRY)
    save_inventory(inventory, transaction_history)

# Main Function
if __name__ == "__main__":
    main()