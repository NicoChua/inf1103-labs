from product import Product
from order_line import OrderLine
from discount_strategy import DiscountStrategy
from no_discount import NoDiscount

class Order:
    def __init__(self, order_id: str, discount: DiscountStrategy | None = None) -> None:
        self.__order_id: str = order_id
        self.__order_lines: list[OrderLine] = []
        self.__discount: DiscountStrategy = discount if discount is not None else NoDiscount()

    def get_order_id(self) -> str:
        return self.__order_id

    def get_discount(self) -> DiscountStrategy:
        return self.__discount

    # Swap the discount strategy on an existing order
    def set_discount(self, discount: DiscountStrategy) -> None:
        self.__discount = discount

    def add_order_line(self, product: Product, quantity: int) -> None:
        order_line = OrderLine(product, quantity)
        self.__order_lines.append(order_line)

    # Total before any discount
    def calculate_subtotal(self) -> float:
        return sum(order_line.calculate_subtotal() for order_line in self.__order_lines)

    def calculate_total(self) -> float:
        return self.__discount.apply(self.calculate_subtotal())

    def display_order(self) -> None:
        print(f"Order ID : {self.__order_id}")
        for order_line in self.__order_lines:
            print(f"  {order_line.get_product().get_name()} x {order_line.get_quantity()}"
                  f" = {order_line.calculate_subtotal()}")
        print(f"Subtotal : {self.calculate_subtotal()}")
        print(f"Discount : {type(self.__discount).__name__}")
        print(f"Total : {self.calculate_total()}")

    def remove_order_line(self, product_id: str) -> bool:
        for order_line in self.__order_lines:
            if order_line.get_product().get_product_id() == product_id:
                self.__order_lines.remove(order_line)
                return True
        return False
