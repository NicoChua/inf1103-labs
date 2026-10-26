class Product:
    def __init__(self, productid, name, price, stock):
        self.__productid = productid
        self.__name = name
        self.__price = price
        self.__stock = stock

    def update_stock(self, quantity):
        self.__stock = quantity

    def display_information(self):
        print(f"Product ID : {self.__productid}")
        print(f"Name : {self.__name}")
        print(f"Price : {self.__price}")
        print(f"Stock : {self.__stock}")