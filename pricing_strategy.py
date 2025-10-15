from exceptions import InvalidCodeError
from order import Order


class PromoCodePricing:
    sales = {
        "SALE10" : 0.1,
        "SALE20" : 0.2,
        "SALE30" : 0.3,
        "SALE50" : 0.5
    }

    def __init__(self, code: str):
        self.code = code

    def __repr__(self):
        return "PromoCodePricing"

    def get_total_after_sale(self, order : Order):
        if self.code in self.sales:
            total = 0
            for item in order.get_items():
                total += item.price * item.quantity
            return total * (1 - self.sales[self.code])
        raise InvalidCodeError

class PizzaDiscount:        # скидка только на пиццу
    sales = {
        "SALE10" : 0.1,
        "SALE20" : 0.2,
        "SALE30" : 0.3,
        "SALE50" : 0.5
    }

    def __init__(self, code: str):
        self.code = code

    def __repr__(self):
        return "PizzaDiscount"

    def get_total_after_sale(self, order : Order):
        if self.code in self.sales:
            total = 0
            for item in order.get_items():
                if "пицца" in item.name.lower():
                    total += item.price * item.quantity * (1 - self.sales[self.code])
                else:
                    total += item.price * item.quantity
            return total
        raise InvalidCodeError

# т.е. каждый вид скидки теперь пишется в отдельном классе и принимает на вход весь заказ,
# что позволяет добавлять скидки на более конкретные вещи





