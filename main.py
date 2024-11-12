import json


class Book: #
    def __init__(self, title: str, author: str, genre: str, price: int, stock: int):
        self.title = title   # название книги.
        self.author = author  # автор книги.
        self.genre = genre   # жанр книги
        self.price = price   # цена книги
        self.stock = stock   # количество книг на складе.

    def update_stock(self, quantity: int):  # Метод для обновления количества книги на складе.
        self.stock += quantity

    def sell(self, quantity: int):  # Метод для продажи определенного количества книги.
        if quantity > self.stock:
            raise ValueError("Недостаточно товара на складе")
        self.stock -= quantity
        return self.price * quantity

    def __str__(self):
        return f"Книга: {self.title}, Автор: {self.author}, Жанр: {self.genre}, Цена: {self.price} руб."

    def to_json(self):
        return {
            "title": self.title,
            "author": self.author,
            "genre": self.genre,
            "price": self.price,
            "stock": self.stock
        }


class Customer:
    def __init__(self, name: str, email: str, phone: str):
        self.name = name  # имя покупателя.
        self.email = email  # электронная почта.
        self.phone = phone  # номер телефона.
        self.orders = []   # список заказов
        self.orders_js = [order.to_json() for order in self.orders]

    def make_order(self, book: Book, quantity: int):  # Метод для создания заказа.
        order = Order(self, book, quantity)
        self.orders.append(order)
        return order

    def __str__(self):
        return f"Покупатель: {self.name}, Email: {self.email}, Телефон: {self.phone}"

    def to_json(self):
        return {
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "orders": self.orders_js
        }


class Order:  # Заказ
    def __init__(self, customer: Customer, book: Book, quantity: int):
        self.customer = customer  # покупатель, который сделал заказ.
        self.book = book  # книга, которая была заказана.
        self.quantity = quantity  # количество заказанных книг.
        self.total_price = book.sell(quantity)
        self.status = 'В процессе'

    def complete_order(self):  # Метод для завершения заказа.
        self.status = 'Завершен'

    def cancel_order(self):  # Метод для отмены заказа.
        self.status = 'Отменен'

    def __str__(self):
        return (f"Заказ: {self.book.title}, Количество: {self.quantity}, Статус: {self.status},"
                f" Сумма: {self.total_price} руб.")

    def to_json(self):
        return {
            "customer": self.customer.to_json(),
            "book": self.book.to_json(),
            "quantity": self.quantity,
            "total_price": self.total_price,
            "status": self.status
        }


class Employee:  # Сотрудник
    def __init__(self, name: str, role: str, salary: int):
        self.name = name  # имя сотрудника.
        self.role = role  # должность сотрудника
        self.salary = salary  # зарплата сотрудника.

    def receive_payment(self, amount: int):  # Метод для выплаты заработной платы сотруднику.
        self.salary += amount

    def __str__(self):
        return f"Сотрудник: {self.name}, Должность: {self.role}, Зарплата: {self.salary} руб."

    def to_json(self):
        return {
            "name": self.name,
            "role": self.role,
            "salary": self.salary
        }


class CashRegister:  # Кассовый аппарат
    def __init__(self):
        self.total_sales = 0

    def process_payment(self, amount: int):  # Метод для обработки платежа
        self.total_sales += amount

    def get_total_sales(self):  # Метод для получения общей суммы всех продаж, сделанных через кассу магазина.
        return self.total_sales

    def to_json(self):
        return {
            "total_sales": self.total_sales
        }


class Category:  # Категория книг
    def __init__(self, name: str):
        self.name = name
        self.books = []

    def add_book(self, book: Book):  # Метод для добавления книги в категорию.
        self.books.append(book)

    def remove_book(self, book: Book):  # Метод для удаления книги из категории.
        self.books.remove(book)

    def list_books(self):  # Метод для получения списка всех книг в категории.
        return [str(book) for book in self.books]

    def __str__(self):
        return f"Категория: {self.name}, Книги: {', '.join([book.title for book in self.books])}"

    def to_json(self):
        return {
            "name": self.name,
            "books": self.books
        }


class Supplier:  # Поставщик
    def __init__(self, name: str, contact_info: str):
        self.name = name  # имя поставщика.
        self.contact_info = contact_info  # контактная информация поставщика.

    def supply_books(self, book: Book, quantity: int):  # Метод для поставки книг в магазин.
        book.update_stock(quantity)
        print(f"Поставщик {self.name} добавил {quantity} копий книги '{book.title}' в магазин.")

    def __str__(self):
        return f"Поставщик: {self.name}, Контакты: {self.contact_info}"

    def to_json(self):
        return {
            "name": self.name,
            "contact_info": self.contact_info
        }


class Inventory:
    def __init__(self):
        self.books = []  # пустой список, в который будут добавляться книги.

    def add_book(self, book: Book):  # Метод для добавления книги в инвентарь магазина.
        self.books.append(book)

    def remove_book(self, book: Book):  # Метод для удаления книги из инвентаря магазина.
        self.books.remove(book)

    def list_books(self):  # Метод для получения списка всех книг в инвентаре магазина.

        return [str(book) for book in self.books]

    def search_by_title(self, title: str):  # Метод для поиска книг по названию.
        return [book for book in self.books if title.lower() in book.title.lower()]

    def search_by_author(self, author: str):  # Метод для поиска книг по автору.
        return [book for book in self.books if author.lower() in book.author.lower()]

    def to_json(self):
        return {
            "books": [book.to_json() for book in self.books]
        }


class Store:
    def __init__(self, name: str, address: str):
        self.name = name  # Название магазина.
        self.address = address  # Адрес магазина.
        self.inventory = Inventory()  # Инвентарь магазина.
        self.cash_register = CashRegister()  # Касса магазина.
        self.employees = []  # Сотрудники.
        self.categories = []  # Категории книг.
        self.orders = []

    def add_employee(self, employee: Employee):  # Метод для добавления сотрудника в магазин.
        self.employees.append(employee)

    def add_order(self, order: Order):  # Метод для добавления сотрудника в магазин.
        self.orders.append(order)

    def add_category(self, category: Category):  # Метод для добавления категории книг в магазин.
        self.categories.append(category)

    def sell_book(self, book: Book, quantity: int):  # Метод для продажи книги.
        total_price = book.sell(quantity)
        self.cash_register.process_payment(total_price)
        return total_price

    def __str__(self):
        return f"Магазин: {self.name}, Адрес: {self.address}"

    def to_json(self):
        return {
            "name": self.name,
            "address": self.address,
            "inventory": self.inventory.to_json(),
            "cash_register": self.cash_register.to_json(),
            "employees": [employee.to_json() for employee in self.employees],
            "categories": self.categories,
            "orders": [order.to_json() for order in self.orders]
        }


# Пример использования:
book1 = Book("Мастер и Маргарита", "Михаил Булгаков", "Роман", 500, 10)
book2 = Book("1984", "Джордж Оруэлл", "Фантастика", 400, 5)

customer1 = Customer("Иван Иванов", "ivan@mail.com", "+79991234567")
employee1 = Employee("Алексей Смирнов", "Продавец", 30000)


store = Store("Книжный мир", "Москва, ул. Пушкина, 1")
store.inventory.add_book(book1)
store.inventory.add_book(book2)
# store.add_employee(employee1.to_json())
store.add_employee(employee1)

order1 = customer1.make_order(book1, 2)
order2 = customer1.make_order(book2, 5)
store.add_order(order1)
store.add_order(order2)
store.sell_book(book1, 2)


print(order1)
with open('json.json', 'w', encoding='utf-8') as jsfile:
    json.dump(store.to_json(), jsfile, ensure_ascii=False, indent = 4)

print(store.inventory.list_books())