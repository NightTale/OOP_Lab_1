from exceptions import InvalidItemError, AlreadyPaidError, IsCancelledError, IsNotCreatedError
from item import Item


class Order:
    id = 1
    def __init__(self):
        self.id = Order.id
        self.items = []
        self.pricing_strategy = None
        self.status = None
        Order.id += 1

    def add_item(self, name: str, price: int, quantity: int):
        if (type(name) == str and len(name) > 0
           and (type(price) in [int, float]) and price > 0
           and type(quantity) == int and quantity > 0):
            self.items.append(Item(name, price, quantity))
            self.status = "Создан (не оплачен)"
        else:
            raise InvalidItemError

    def set_pricing_strategy(self, strategy):
        self.pricing_strategy = strategy

    def get_total(self):
        total = 0
        for item in self.items:
            total += item.price * item.quantity
        if self.pricing_strategy is None:
            return total
        return f"Итоговая стоимость заказа: {total * (1 - self.pricing_strategy.sale())} руб."

    def get_items(self):
        return self.items

    def pay(self, payment_type):
        if self.status == "Создан (не оплачен)":
            self.status = "Оплачен"
        elif self.status == "Оплачен":
            raise AlreadyPaidError
        elif self.status == "Отменён":
            raise IsCancelledError
        else:
            raise IsNotCreatedError

    def get_status(self):
        return f"Статус заказа: {self.status}"

    def cancel(self):
        if self.status == "Отменён":
            raise IsCancelledError
        elif self.status == "Оплачен":
            raise AlreadyPaidError
        else:
            self.status = "Отменён"









