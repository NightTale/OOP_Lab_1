from exceptions import *
from json_exporter import JsonExporter
from payment import *
from pricing_strategy import *

order = Order()

try:
    order.add_item("Пицца Маргарита", 500, 2)
    order.add_item("Пельмени", 400, 1)
except InvalidItemError as e:
    print(e)

order.set_pricing_strategy(PizzaDiscount("SALE20"))

for item in order.get_items():
    print(item)

print(order.get_total())
print(order.get_status())

payment = CardPayment
order.pay(payment)

print(order.get_status())

exporter = JsonExporter()
print(exporter.export(order))
