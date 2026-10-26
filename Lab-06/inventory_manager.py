""" 
INF1103 Week 5 - Inventory Manager
"""
import json
from product import Product
from inventory import Inventory

# Global Constants
INVENTORY_FILE = "inventory.json"

# Loads Inventory from inventory.json
def load_inventory():
    inventory = Inventory()
    status = False

    try:
        with open(INVENTORY_FILE, "r") as file:
            for item in json.load(file):
                product = Product(item["id"], item["name"], float(item["price"]), int(item["stock"]))
                inventory.add_product(product)
            status = True
    except (FileNotFoundError, json.JSONDecodeError, KeyError, ValueError):
        status = False

    return inventory, status

# Stores inventory into inventory.json
def save_inventory(inventory):
    try:
        with open(INVENTORY_FILE, "w") as file:
            json.dump(inventory.to_list(), file, indent=4)
        return True
    except Exception as e:
        print("Unable to save inventory")
        return False


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
    exit_program = False
    inventory, status = load_inventory()

    if status:
        print("inventory.json found.")
        print("Inventory loaded successfully.")
    else:
        print("Failed to load inventory.")

    # Main Program to get user input
    while not exit_program:
        print("\n============================================")
        print("INVENTORY MANAGEMENT SYSTEM")
        print("============================================\n")

        # Menu
        user_input = get_valid_input()

        if user_input == "1":
            inventory.display_all()
        elif user_input == "2":
            print("Add New Product")
            product_id = input("Product ID: ")
            name = input("Product Name: ")
            try:
                price = float(input("Price: "))
                stock = int(input("Stock Quantity: "))
            except ValueError:
                print("Invalid price or stock. Product not added")
                continue
            if price < 0 or stock < 0:
                print("Price and stock cannot be negative. Product not added")
                continue
            new_product = Product(product_id, name, price, stock)
            inventory.add_product(new_product)
        elif user_input == "3":
            print("Update Stock")
            product_id = input("Enter Product ID: ")
            p = inventory.search_product(product_id)
            if p:
                try:
                    updated_stock = int(input("Enter New Stock Quantity: "))
                except ValueError:
                    print("Invalid stock quantity. Stock not updated")
                    continue
                if p.update_stock(updated_stock):
                    print("Stock updated successfully!")
                else:
                    print("Stock cannot be negative. Stock not updated")
        elif user_input == "4":
            print("Search Product")
            product_id = input("Enter Product ID: ")
            inventory.search_product(product_id)
        elif user_input == "5":
            if save_inventory(inventory):
                print("Inventory saved successfully")
        elif user_input == "6":
            print("Saving inventory before exit...")
            if save_inventory(inventory):
                print("Inventory saved successfully")
            print("\nThank you for using Inventory Management System.\nProgram terminated")
            break

# Main Function
if __name__ == "__main__":
    main()