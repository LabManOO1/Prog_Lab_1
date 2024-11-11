class Book: #
    def __init__(self, title, author, genre, price, stock):
        self.title = title   #  название книги.
        self.author = author #  автор книги.
        self.genre = genre   #  жанр книги
        self.price = price   #  цена книги
        self.stock = stock   #  количество книг на складе.

    def update_stock(self, quantity):  #  Метод для обновления количества книги на складе.
        self.stock += quantity

    def sell(self, quantity):  #  Метод для продажи определенного количества книги.
        if quantity > self.stock:
            raise ValueError("Недостаточно товара на складе")
        self.stock -= quantity
        return self.price * quantity

    def __str__(self):
        return f"Книга: {self.title}, Автор: {self.author}, Жанр: {self.genre}, Цена: {self.price} руб."


class Customer:
    def __init__(self, name, email, phone):
        self.name = name  #  имя покупателя.
        self.email = email  #  электронная почта.
        self.phone = phone  #  номер телефона.
        self.orders = []   #  список заказов

    def make_order(self, book, quantity):  #  Метод для создания заказа.
        order = Order(self, book, quantity)
        self.orders.append(order)
        return order

    def __str__(self):
        return f"Покупатель: {self.name}, Email: {self.email}, Телефон: {self.phone}"


class Order:  #  Заказ
    def __init__(self, customer, book, quantity):
        self.customer = customer  #  покупатель, который сделал заказ.
        self.book = book  #  книга, которая была заказана.
        self.quantity = quantity  #  количество заказанных книг.
        self.total_price = book.sell(quantity)
        self.status = 'В процессе'

    def complete_order(self):  #  Метод для завершения заказа.
        self.status = 'Завершен'

    def cancel_order(self):  #  Метод для отмены заказа.
        self.status = 'Отменен'

    def __str__(self):
        return f"Заказ: {self.book.title}, Количество: {self.quantity}, Статус: {self.status}, Сумма: {self.total_price} руб."


class Employee:  #  Сотрудник
    def __init__(self, name, role, salary):
        self.name = name  #  имя сотрудника.
        self.role = role  #  должность сотрудника
        self.salary = salary  #  зарплата сотрудника.

    def receive_payment(self, amount):  #  Метод для выплаты заработной платы сотруднику.
        self.salary += amount

    def __str__(self):
        return f"Сотрудник: {self.name}, Должность: {self.role}, Зарплата: {self.salary} руб."


class CashRegister:  #  Кассовый аппарат
    def __init__(self):
        self.total_sales = 0

    def process_payment(self, amount):  #  Метод для обработки платежа
        self.total_sales += amount

    def get_total_sales(self):  #  Метод для получения общей суммы всех продаж, сделанных через кассу магазина.
        return self.total_sales


class Category:  #  Категория книг
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):  #  Метод для добавления книги в категорию.
        self.books.append(book)

    def remove_book(self, book):  #  Метод для удаления книги из категории.
        self.books.remove(book)

    def list_books(self):  #  Метод для получения списка всех книг в категории.
        return [str(book) for book in self.books]

    def __str__(self):
        return f"Категория: {self.name}, Книги: {', '.join([book.title for book in self.books])}"


class Supplier:  #  Поставщик
    def __init__(self, name, contact_info):
        self.name = name  #  имя поставщика.
        self.contact_info = contact_info  #  контактная информация поставщика.

    def supply_books(self, book, quantity):  #  Метод для поставки книг в магазин.
        book.update_stock(quantity)
        print(f"Поставщик {self.name} добавил {quantity} копий книги '{book.title}' в магазин.")

    def __str__(self):
        return f"Поставщик: {self.name}, Контакты: {self.contact_info}"


class Inventory:
    def __init__(self):
        self.books = []  #  пустой список, в который будут добавляться книги.

    def add_book(self, book):  #  Метод для добавления книги в инвентарь магазина.
        self.books.append(book)

    def remove_book(self, book):  #  Метод для удаления книги из инвентаря магазина.
        self.books.remove(book)

    def list_books(self):  #  Метод для получения списка всех книг в инвентаре магазина.

        return [str(book) for book in self.books]

    def search_by_title(self, title):  #  Метод для поиска книг по названию.
        return [book for book in self.books if title.lower() in book.title.lower()]

    def search_by_author(self, author):  #  Метод для поиска книг по автору.
        return [book for book in self.books if author.lower() in book.author.lower()]


class Store:
    def __init__(self, name, address):
        self.name = name  #  Название магазина.
        self.address = address  #  Адрес магазина.
        self.inventory = Inventory()  #  Инвентарь магазина.
        self.cash_register = CashRegister()  #  Касса магазина.
        self.employees = []  #  Сотрудники.
        self.categories = []  #  Категории книг.

    def add_employee(self, employee):  #  Метод для добавления сотрудника в магазин.
        self.employees.append(employee)

    def add_category(self, category):  #  Метод для добавления категории книг в магазин.
        self.categories.append(category)

    def sell_book(self, book, quantity):  #  Метод для продажи книги.
        total_price = book.sell(quantity)
        self.cash_register.process_payment(total_price)
        return total_price

    def __str__(self):
        return f"Магазин: {self.name}, Адрес: {self.address}"

