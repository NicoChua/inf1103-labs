from product import Product

class Inventory:
    def __init__(self) -> None:
        self.__products: list[Product] = []

    def get_products(self) -> list[Product]:
        return list(self.__products)   # a copy, so outsiders can't modify the real list

    def add_product(self, product: Product) -> None:
        if self.find_product(product.get_product_id()) is not None:
            print("Product not added")
            return
        self.__products.append(product)
        print("Product added successfully!\n")

    def remove_product(self, product_id: str) -> bool:
        product = self.find_product(product_id)
        if product is None:
            return False
        self.__products.remove(product)
        return True

    def find_product(self, product_id: str) -> Product | None:
        for product in self.__products:
            if product.get_product_id() == product_id:
                return product
        return None

    def display_all(self) -> None:
        for product in self.__products:
            product.display_information()
            print(product.get_fulfilment_info())
            print()

    # Returns all products as a list of dictionaries
    def to_list(self) -> list[dict]:
        return [product.to_dict() for product in self.__products]
