class OrderSubsystem:
    def __init__(self):
        self.orders = []

    def create_order(self, user, products):
        order = Order(user, products, "В обработке")
        self.orders.append(order)

    def update_order_status(self, order, status):
        order.delivery_status = status

    def delete_order(self, order):
        self.orders.remove(order)