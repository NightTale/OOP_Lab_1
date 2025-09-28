from order import Order

class JsonExporter:
    def export(self, order: Order):
        return {
            "id" : order.id,
            "items" : order.items,
            "pricing_strategy" : order.pricing_strategy,
            "status" : order.status
        }
