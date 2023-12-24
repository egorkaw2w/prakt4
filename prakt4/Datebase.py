class Database:
    def __init__(self):
        self.conn = sqlite3.connect(':memory:')  # Создание базы данных в памяти
        self.cursor = self.conn.cursor()

        self.cursor.execute('''
            CREATE TABLE users (name TEXT, email TEXT, password TEXT)
        ''')
        self.cursor.execute('''
            CREATE TABLE products (name TEXT, price REAL, category TEXT)
        ''')
        self.cursor.execute('''
            CREATE TABLE orders (user TEXT, products TEXT, delivery_status TEXT)
        ''')

    def save_user(self, user):
        if not validators.email(user.email):
            raise ValueError("Некорректный email")
        self.cursor.execute('''
            INSERT INTO users VALUES (?, ?, ?)
        ''', (user.name, user.email, user.password))
        self.conn.commit()

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