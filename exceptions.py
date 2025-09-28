class InvalidItemError(Exception):
    def __str__(self):
        return "Ошибка: некорректные данные позиции"

class InvalidPromoCodeError(Exception):
    def __str__(self):
        return "Нет такого промокода"

class AlreadyPaidError(Exception):
    def __str__(self):
        return "Заказ уже оплачен"

class IsCancelledError(Exception):
    def __str__(self):
        return "Заказ отменён"

class IsNotCreatedError(Exception):
    def __str__(self):
        return "Заказ не создан"
