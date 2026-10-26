class Inventory:
    def __init__(self):
        self.__inventory = []

    # Add Product to inventory
    def add_product(self, product):
        for p in self.__inventory:
            if p._product_id == product._product_id:
                print("Product not added")
                break
        else:
            self.__inventory.append(product)
            print("Product added successfully!\n")

    def search_product(self, product_id):
        for p in self.__inventory:
            if p._product_id == product_id:
                p.display_information()
                return p
        else:
            print("Product not found")

    def display_all(self):
        for p in self.__inventory:
            p.display_information()

    # Returns all products as a list of dictionaries
    def to_list(self):
        return [p.to_dict() for p in self.__inventory]

