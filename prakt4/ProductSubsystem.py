class ProductSubsystem:
    def __init__(self):
        self.products = []

    def add_product(self, name, price, category):
        product = Product(name, price, category)
        self.products.append(product)

    def update_product(self, name, new_price):
        for product in self.products:
            if product.name == name:
                product.price = new_price

    def delete_product(self, name):
        self.products = [product for product in self.products if product.name != name]

    def filter_products(self, category):
        filtered_products = [product for product in self.products if product.category == category]
        return filtered_products