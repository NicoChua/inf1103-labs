from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, product_id, name, price, stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock

    # Getters
    def get_product_id(self):
        return self.__product_id
    
    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_stock(self):
        return self.__stock


    # Only accepts non-negative stock, returns True if updated
    def update_stock(self, quantity):
        if quantity < 0:
            return False
        self.__stock = quantity
        return True


    def display_information(self):
        print(f"Product ID : {self.__product_id}")
        print(f"Name : {self.__name}")
        print(f"Price : {self.__price}")
        print(f"Stock : {self.__stock}")

    @abstractmethod
    def get_fulfilment_info(self) -> str:
        """Return delivery/fulfilment information for this product type"""


    # Returns product data as a dictionary for saving to JSON
    def to_dict(self):
        return {"id": self.__product_id, "name": self.__name, "price": self.__price, "stock": self.__stock}
        