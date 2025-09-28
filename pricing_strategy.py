from exceptions import InvalidPromoCodeError


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

    def sale(self):
        if self.code in self.sales:
            return self.sales[self.code]
        raise InvalidPromoCodeError






