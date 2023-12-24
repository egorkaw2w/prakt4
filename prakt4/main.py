import sqlite3
from User import User
from UserSubsystem import UserSubsystem
from Order import Order
from OrderSubsystem import OrderSubsystem
from Product import Product
from ProductSubsystem import ProductSubsystem
from ShoppingCart import ShoppingCart
from Datebase import Database

class Database:
    def __init__(self):
        self.conn = sqlite3.connect(':memory:')  # Создание базы данных в памяти
        self.cursor = self.conn.cursor()

        # Создание таблиц
        self.cursor.execute('''
            CREATE TABLE users (name TEXT, email TEXT, password TEXT)
        ''')
        self.cursor.execute('''
            CREATE TABLE products (name TEXT, price REAL, category TEXT)
        ''')
        self.cursor.execute('''
            CREATE TABLE orders (user TEXT, products TEXT, delivery_status TEXT)
        ''')



    def save_product(self, product):
        self.cursor.execute('''
            INSERT INTO products VALUES (?, ?, ?)
        ''', (product.name, product.price, product.category))
        self.conn.commit()

    def save_order(self, order):
        self.cursor.execute('''
            INSERT INTO orders VALUES (?, ?, ?)
        ''', (order.user.email, str(order.products), order.delivery_status))
        self.conn.commit()

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

class UserSubsystem:
    def __init__(self):
        self.users = []

    def register_user(self, name, email, password):
        user = User(name, email, password)
        self.users.append(user)

    def authenticate_user(self, email, password):
        for user in self.users:
            if user.email == email and user.password == password:
                return True
        return False

class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

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


class Order:
    def __init__(self, user, products, delivery_status):
        self.user = user
        self.products = products
        self.delivery_status = delivery_status

class OrderSubsystem:
    def __init__(self):
        self.orders = []

    def create_order(self, user, products):
        order = Order(user, products, "делается")
        self.orders.append(order)

    def update_order_status(self, order, status):
        order.delivery_status = status

    def delete_order(self, order):
        self.orders.remove(order)

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product):
        self.items.append(product)

    def remove_item(self, product):
        self.items.remove(product)

    def view_cart(self):
        return self.items



user_subsystem = UserSubsystem()
user_subsystem.register_user("John Doe", "johndoe@example.com", "password123")
user_subsystem.register_user("Jane Smith", "janesmith@example.com", "pass456")

authenticated = user_subsystem.authenticate_user("johndoe@example.com", "password123")
if authenticated:
    print("Пользователь авторизован.")
else:
    print("Неверные  данные.")

product_subsystem = ProductSubsystem()
product_subsystem.add_product("Пк", 2000, "Электроника")
product_subsystem.add_product("флешка", 20, "Компьютерные аксессуары")
product_subsystem.add_product("майка", 30, "Одежда")

filtered_products = product_subsystem.filter_products("Электроника")
for product in filtered_products:
    print(product.name, product.price)

order_subsystem = OrderSubsystem()
cart = ShoppingCart()
cart.add_item(product_subsystem.products[0])
cart.add_item(product_subsystem.products[1])
order_subsystem.create_order(user_subsystem.users[0], cart.view_cart())

# Обновление статуса заказа
order_subsystem.update_order_status(order_subsystem.orders[0], "Доставлен")

# Удаление заказа
order_subsystem.delete_order(order_subsystem.orders[0])

