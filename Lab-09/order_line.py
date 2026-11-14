from product import Product

class OrderLine:
    def __init__(self, product: Product, quantity: int) -> None:
        # Validation
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        self.__product: Product = product
        self.__quantity: int = quantity

    def get_product(self) -> Product:
        return self.__product

    def get_quantity(self) -> int:
        return self.__quantity
    
    def calculate_subtotal(self) -> float:
        return self.__product.get_price() * self.__quantity