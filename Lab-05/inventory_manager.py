""" 
INF1103 Week 5 - Inventory Manager
"""
import json

# Global Constants
INVENTORY_FILE = "inventory.json"

# Loads Inventory from inventory.json
def load_inventory():
    inventory = []
    status = False

    try:
        with open(INVENTORY_FILE, "r") as file:
            inventory = json.load(file)
            status = True
    except (FileNotFoundError, json.JSONDecodeError):
        status = False

    return inventory, status

# Stores inventory into inventory.json
def save_inventory(inventory):
    try:
        with open(INVENTORY_FILE, "w") as file:
            json.dump(inventory, file, indent=4)
    except Exception as e:
        print("Unable to save inventory")

# Search for Product ID
def search_product(inventory, product_id):
    for product in inventory:
        if product['id'] == product_id:
            return product
    else:
        return None

# Add Product to inventory
def add_product(inventory, product_id, name, price, stock):
    for product in inventory:
        if product['id'] == product_id:
            return False
    else:
        inventory.append(product)
        save_inventory(inventory)
        return True

# Update Product in inventory
def update_stock(inventory, product_id, new_stock):
    for product in inventory:
        if product['id'] == product_id:
            return True
    else:
        return False

# Display Inventory
def display_all(inventory):
    for product in inventory:
        print(f"ID: {product['id']} | Name: {product['name']} | Price: {product['price']} | Stock: {product['stock']}")

# Gets and validates user input
def get_valid_input():
    print("----------MENU----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("-------------------------")
    user_input = input("Enter Option: ")
    if user_input.isdigit() != True:
        print("Please input a number")
        return None
    return user_input

def main():
    # Variables
    inventory = 0
    exit_program = False

    # Main Program to get user input
    while not exit_program:
        print("============================================")
        print("INVENTORY MANAGEMENT SYSTEM")
        print("============================================")

        inventory, status = load_inventory()
        if status:
            print("inventory.json found.")
            print("Inventory loaded successfully.")
        else:
            print("Failed to load inventory.")
            # break

        # Menu
        user_input = get_valid_input()


        
    #     if stockQty == "quit":
    #         exit_program = True
    #     elif stockQty == None:
    #         continue
    #     else:
    #         if inventory >= MAX_CAPACITY:
    #             break
    #         inventory = process_delivery(inventory, stockQty)
    #         tax_amount += calculate_tax(stockQty)
    #         transaction_history.append(f"\n{stockQty}")

    # # Final Output
    # generate_report(inventory, FAILED_ENTRY)
    # save_inventory(inventory, transaction_history)

# Main Function
if __name__ == "__main__":
    main()