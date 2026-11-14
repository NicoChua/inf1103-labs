from abc import ABC, abstractmethod
from supplier import Supplier

class Product(ABC):
    def __init__(self, product_id: str, name: str, price: float,
                 stock: int, supplier: Supplier) -> None:
        self.__product_id: str = product_id
        self.__name: str = name
        self.__price: float = price
        self.__stock: int = stock
        self.supplier: Supplier = supplier

    # Getters
    def get_product_id(self) -> str:
        return self.__product_id

    def get_name(self) -> str:
        return self.__name

    def get_price(self) -> float:
        return self.__price

    def get_stock(self) -> int:
        return self.__stock


    # Only accepts non-negative stock, returns True if updated
    def update_stock(self, quantity: int) -> bool:
        if quantity < 0:
            return False
        self.__stock = quantity
        return True


    def display_information(self) -> None:
        print(f"Product ID : {self.__product_id}")
        print(f"Name : {self.__name}")
        print(f"Price : {self.__price}")
        print(f"Stock : {self.__stock}")
        print(f"Supplier : {self.supplier.get_name()}")

    @abstractmethod
    def get_fulfilment_info(self) -> str:
        """Return delivery/fulfilment information for this product type"""


    # Returns product data as a dictionary for saving to JSON
    def to_dict(self) -> dict:
        return {"id": self.__product_id, "name": self.__name, "price": self.__price,
                "stock": self.__stock, "supplier": self.supplier.to_dict()}
