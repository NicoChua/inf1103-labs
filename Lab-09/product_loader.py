import csv
from inventory import Inventory
from supplier import Supplier
from product_factory import ProductFactory


# 5.2 Reads products from a CSV file, creates each through ProductFactory and adds it to inventory.
def load_products(path: str, inventory: Inventory, supplier: Supplier) -> None:
    try:
        file = open(path, newline="")
    except FileNotFoundError:
        print(f"Products file not found: {path}")
    else:
        loaded = 0
        with file:
            reader = csv.reader(file)
            next(reader, None)   # skip the header row
            for row in reader:
                # Each row gets its own try, so one bad row doesn't stop the rest
                try:
                    product_type, product_id, name, price, stock_quantity = row
                    product = ProductFactory.create(product_type, product_id, name,
                                                    float(price), int(stock_quantity), supplier)
                except ValueError as e:
                    print(f"Skipped row {row}: {e}")
                    continue
                before = len(inventory.get_products())
                inventory.add_product(product)
                if len(inventory.get_products()) > before:   # not added if the ID already exists
                    loaded += 1
        print(f"{loaded} products loaded.")
    finally:
        print("Load attempt finished.")
