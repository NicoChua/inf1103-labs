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
            print(f"ID: {product['id']} | Name: {product['name']} | Price: {product['price']} | Stock: {product['stock']}")
            return product
    else:
        print("Product not found")
        return None

# Add Product to inventory
def add_product(inventory, product_id, name, price, stock):
    new_product = {
        "id": product_id,
        "name": name,
        "price": round(float(price), 2),
        "stock": round(float(stock), 2)
    }
    for product in inventory:
        if product['id'] == product_id:
            print("Product not added")
            return False
    else:
        inventory.append(new_product)
        print("\Product added successfully!\n")
        return True

# Update Product in inventory
def update_stock(inventory, product_id):
    for product in inventory:
        if product['id'] == product_id:
            print(f"Product Found: \nName: {product['name']} \nCurrent Stock: {product['stock']}")
            new_stock = input("New Stock Quantity: ")
            product['stock'] = int(new_stock)
            print("\nStock Updated successfully!\n")
            return True
    else:
        print("Stock not updated")
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
    inventory = []
    exit_program = False
    inventory, status = load_inventory()

    # Main Program to get user input
    while not exit_program:
        print("\n============================================")
        print("INVENTORY MANAGEMENT SYSTEM")
        print("============================================\n")

        if status:
            print("inventory.json found.")
            print("Inventory loaded successfully.")
        else:
            print("Failed to load inventory.")
            # break

        # Menu
        user_input = get_valid_input()

        if user_input == "1":
            display_all(inventory)
        elif user_input == "2":
            print("Add New Product")
            product_id = input("Product ID: ")
            name = input("Product Name: ")
            price = input("Price: ")
            stock = input("Stock Quantity: ")
            add_product(inventory, product_id, name, price, stock)
        elif user_input == "3":
            print("Update Stock")
            product_id = input("Product ID: ")
            update_stock(inventory, product_id)
        elif user_input == "4":
            print("Search Product")
            product_id = input("Enter Product ID: ")
            search_product(inventory, product_id)
        elif user_input == "5":
            save_inventory(inventory)
        elif user_input == "6":
            print("Saving inventory before exit...")
            save_inventory(inventory)
            print("Inventory saved successfully")
            print("\nThank you for using Inventory Management System.\nProgram terminated")
            break

# Main Function
if __name__ == "__main__":
    main()