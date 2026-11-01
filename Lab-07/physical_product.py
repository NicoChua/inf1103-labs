# Child Class
from product import Product
from can_be_shipped import CanBeShipped

class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        self.__weight = weight

    def get_weight(self)->float:
        return self.__weight

    def calculate_shipping_cost(self) -> float:
        return max(0.0, self.__weight * 2.5)

    def display_information(self):
        super().display_information()
        print(f"Weight : {self.__weight}")

    def get_fulfilment_info(self):
        return "Requires physical shipping."

    def to_dict(self):
        data = super().to_dict()
        data["type"] = "physical"
        data["weight"] = self.__weight
        return data
