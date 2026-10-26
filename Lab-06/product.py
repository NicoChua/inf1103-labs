class Product:
    def __init__(self, product_id, name, price, stock):
        self._product_id = product_id
        self._name = name
        self._price = price
        self._stock = stock


    # Only accepts non-negative stock, returns True if updated
    def update_stock(self, quantity):
        if quantity < 0:
            return False
        self._stock = quantity
        return True


    def display_information(self):
        print(f"Product ID : {self._product_id}")
        print(f"Name : {self._name}")
        print(f"Price : {self._price}")
        print(f"Stock : {self._stock}")


    # Returns product data as a dictionary for saving to JSON
    def to_dict(self):
        return {"id": self._product_id, "name": self._name, "price": self._price, "stock": self._stock}
        