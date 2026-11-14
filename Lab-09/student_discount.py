from discount_strategy import DiscountStrategy

class StudentDiscount(DiscountStrategy):
    STUDENT_RATE: float = 5.0

    def apply(self, total: float) -> float:
        return total * (1 - self.STUDENT_RATE / 100)
