import json
from product import Product
from product_factory import ProductFactory
from inventory import Inventory
from supplier import Supplier

# Global Constants
INVENTORY_FILE = "inventory.json"
DEFAULT_SUPPLIER = Supplier("S000", "Unknown Supplier", "N/A")


# Returns the existing Supplier with this ID, or creates and registers a new one.
def get_or_create_supplier(suppliers: dict[str, Supplier], supplier_id: str,
                           name: str, contact_email: str) -> Supplier:
    if supplier_id not in suppliers:
        suppliers[supplier_id] = Supplier(supplier_id, name, contact_email)
    return suppliers[supplier_id]


# Loads Inventory from inventory.json
def load_inventory(suppliers: dict[str, Supplier]) -> tuple[Inventory, bool]:
    inventory = Inventory()

    try:
        with open(INVENTORY_FILE, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        print(f"{INVENTORY_FILE} not found. Starting with an empty inventory.")
        return inventory, True
    except (json.JSONDecodeError, OSError) as e:
        print(f"Could not read {INVENTORY_FILE}: {e}")
        return inventory, False

    for item in data:
        try:
            if "supplier" in item:
                s = item["supplier"]
                supplier = get_or_create_supplier(suppliers, s["id"], s["name"], s["contact_email"])
            else:
                supplier = DEFAULT_SUPPLIER

            # The factory decides which subclass to build (raises ValueError for unknown types)
            product: Product = ProductFactory.create(
                item["type"], item["id"], item["name"], float(item["price"]),
                int(item["stock"]), supplier,
                weight=float(item.get("weight", 0.0)),
                download_size=float(item.get("download_size", 0.0)))
        except (KeyError, ValueError, TypeError) as e:
            print(f"Invalid product entry {item}: {e}. Skipped")
            continue
        inventory.add_product(product)

    return inventory, True


# Stores inventory into inventory.json
def save_inventory(inventory: Inventory) -> bool:
    try:
        with open(INVENTORY_FILE, "w") as file:
            json.dump(inventory.to_list(), file, indent=4)
        return True
    except OSError:
        print("Unable to save inventory")
        return False


# Gets and validates user input
def get_valid_input() -> str | None:
    print("----------MENU----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Remove Product")
    print("6. Save Inventory")
    print("7. Exit")
    print("-------------------------")
    user_input = input("Enter Option: ")
    if not user_input.isdigit():
        print("Please input a number")
        return None
    return user_input


# Asks for a supplier ID
def get_supplier_from_input(suppliers: dict[str, Supplier]) -> Supplier:
    supplier_id = input("Supplier ID: ")
    if supplier_id in suppliers:
        print(f"Using existing supplier: {suppliers[supplier_id].get_name()}")
        return suppliers[supplier_id]
    name = input("Supplier Name: ")
    contact_email = input("Supplier Contact Email: ")
    return get_or_create_supplier(suppliers, supplier_id, name, contact_email)


# Add Product
def create_product_from_input(suppliers: dict[str, Supplier]) -> Product | None:
    print("Select Product Type")
    print("1. Physical Product")
    print("2. Digital Product")
    product_type = input("Enter Option: ")
    if product_type not in ("1", "2"):
        print("Invalid product type. Product not added")
        return None

    product_id = input("Product ID: ")
    name = input("Product Name: ")
    try:
        price = float(input("Price: "))
        stock = int(input("Stock Quantity: "))
        if product_type == "1":
            extra = float(input("Weight (kg): "))
        else:
            extra = float(input("Download Size (MB): "))
    except ValueError:
        print("Invalid input. Product not added")
        return None

    if price < 0 or stock < 0 or extra < 0:
        print("Values cannot be negative. Product not added")
        return None

    supplier = get_supplier_from_input(suppliers)

    if product_type == "1":
        return ProductFactory.create("physical", product_id, name, price, stock, supplier,
                                     weight=extra)
    else:
        return ProductFactory.create("digital", product_id, name, price, stock, supplier,
                                     download_size=extra)


def main() -> None:
    # Variables
    suppliers: dict[str, Supplier] = {}
    inventory, status = load_inventory(suppliers)

    # If the file exists but could not be read, don't overwrite it with an empty inventory
    can_save = status
    if status:
        print("Inventory loaded successfully.")
    else:
        print("Failed to load inventory. Saving is disabled to protect the existing file.")

    # Main Program to get user input
    while True:
        print("\n============================================")
        print("INVENTORY MANAGEMENT SYSTEM")
        print("============================================\n")

        # Menu
        user_input = get_valid_input()

        if user_input == "1":
            inventory.display_all()
        elif user_input == "2":
            print("Add New Product")
            new_product = create_product_from_input(suppliers)
            if new_product:
                inventory.add_product(new_product)
        elif user_input == "3":
            print("Update Stock")
            product_id = input("Enter Product ID: ")
            p = inventory.find_product(product_id)
            if p is None:
                print("Product not found")
                continue
            p.display_information()
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
            p = inventory.find_product(product_id)
            if p is None:
                print("Product not found")
            else:
                p.display_information()
                print(p.get_fulfilment_info())
        elif user_input == "5":
            print("Remove Product")
            product_id = input("Enter Product ID: ")
            if inventory.remove_product(product_id):
                print("Product removed from inventory")
            else:
                print("Product not found")
        elif user_input == "6":
            if not can_save:
                print("Saving is disabled because the inventory file could not be loaded")
            elif save_inventory(inventory):
                print("Inventory saved successfully")
        elif user_input == "7":
            if can_save:
                print("Saving inventory before exit...")
                if save_inventory(inventory):
                    print("Inventory saved successfully")
            print("\nThank you for using Inventory Management System.\nProgram terminated")
            break
        elif user_input is not None:
            print("Invalid option. Please choose 1-7")

# Main Function
if __name__ == "__main__":
    main()
