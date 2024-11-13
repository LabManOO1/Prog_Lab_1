import json
import os

# import Config
PATH = "json.json"


class DataBase:
    def __init__(self, path: str):
        if os.path.isfile(path):
            self.__path = path
            self.dt = self.db()

    def db(self):
        with open(self.__path, 'r') as jsfile:
            return json.load(jsfile)

    def write_db(self, dt: dict):
        with open(self.__path, 'w', encoding="utf-8") as jsfile:
            json.dump(dt, jsfile, indent=3)


class Book:  #
    def __init__(self, title: str, author: str, genre: str, price: int, stock: int):
        self.title = title  # название книги.
        self.author = author  # автор книги.
        self.genre = genre  # жанр книги
        self.price = price  # цена книги
        self.stock = stock  # количество книг на складе.

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

    def __str__(self):
        return f"Покупатель: {self.name}, Email: {self.email}, Телефон: {self.phone}"

    def to_json(self):
        return {
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            # "orders": self.orders_js
        }


class Order:  # Заказ
    def __init__(self, customer: Customer, books: list, quantity: int, total_price: int):
        self.customer = customer  # покупатель, который сделал заказ.
        self.book = books  # список заказанных книг
        self.quantity = quantity  # количество заказанных книг.
        self.total_price = total_price
        self.status = 'В процессе'

    def complete_order(self):  # Метод для завершения заказа.
        self.status = 'Завершен'

    def cancel_order(self):  # Метод для отмены заказа.
        self.status = 'Отменен'

    def to_json(self):
        return {
            "customer": self.customer.to_json(),
            "books": self.book,
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
        self.total_sales = dt["cash_register"]

    def process_payment(self, amount: int):  # Метод для обработки платежа
        self.total_sales += amount
        dt["cash_register"] += amount

    def get_total_sales(self):  # Метод для получения общей суммы всех продаж, сделанных через кассу магазина.
        return self.total_sales

    def to_json(self):
        return {
            "total_sales": self.total_sales
        }


class Inventory:
    def __init__(self):

        self.books = [Book(book["title"], book["author"], book["genre"], book["price"], book["stock"]) for book in
                      dt["inventory"]["books"]]  # пустой список, в который будут добавляться книги.

    def add_book(self):  # Метод для добавления книги в инвентарь магазина.

        if len(dt["inventory"]["books"]) == 0:
            title = input("Введите название книги  ")
            author = input("Введите автора книги  ")
            genre = input("Введите жанр книги  ")
            price = int(input("Введите цену книги  "))
            stock = int(input("Введите кол-во книг, которое хотите добавить  "))
            book = Book(title, author, genre, price, stock)

            dt["inventory"]["books"].append(book.to_json())

            dtb.write_db(dt)

            self.books.append(book)
            return
        title = input("Введите название книги  ")
        author = input("Введите автора книги  ")
        for i in range(len(dt["inventory"]["books"])):
            if (dt["inventory"]["books"][i]["title"] == title) and (dt["inventory"]["books"][i].author == author):
                print("Книга уже есть в инвентаре")
                stock = int(input("Введите кол-во книг, которое хотите добавить  "))
                dt["inventory"]["books"][i]["stock"] += stock
                dtb.write_db(dt)
            else:
                genre = input("Введите жанр книги  ")
                price = int(input("Введите цену книги  "))
                stock = int(input("Введите кол-во книг, которое хотите добавить  "))
                book = Book(title, author, genre, price, stock)
                dt["inventory"]["books"].append(book.to_json())
                dtb.write_db(dt)

                self.books.append(book)

    def change_stock(self):
        name = input("Введите название книги, количество которой хотите изменить  ")
        stock = int(input("Введите новое количество книг  "))
        for i in range(len(dt["inventory"]["books"])):
            if name == dt["inventory"]["books"][i]["title"]:
                dt["inventory"]["books"][i]["stock"] = stock
                self.books[i].stock = stock
                dtb.write_db(dt)
                return
        return print("Такой книги нет")

    def remove_book(self):  # Метод для удаления книги из инвентаря магазина.
        if len(dt["inventory"]["books"]) == 0:
            print("Список книг пуст")
            return

        title = input("Введите название книги  ")
        author = input("Введите автора книги  ")
        flag = False

        for i in range(len(dt["inventory"]["books"])):
            if (dt["inventory"]["books"][i]["title"] == title) and (dt["inventory"]["books"][i]["author"] == author):
                flag = True
                stock = int(input("Введите кол-во книг, которое хотите удалить  "))

                if dt["inventory"]["books"][i]["stock"] < stock:
                    print("В инвентаре нет столько книг")

                elif (dt["inventory"]["books"][i]["stock"] - stock) == 0:

                    dt["inventory"]["books"].pop(i)
                    dtb.write_db(dt)
                    self.books.pop(i)
                    return

                else:
                    self.books[i].stock -= stock
                    dt["inventory"]["books"][i]["stock"] -= stock
                    dtb.write_db(dt)
                    return

        if not flag:
            print("Такой книги нет в инвентаре")

    def get_books(self):
        return self.books

    def check_book(self, book_title: str):
        for i in range(len(self.books)):
            if book_title == self.books[i].title:
                return True
        return False

    def search__by_title_one(self, title: str):
        for book in self.books:
            if book.title == title:
                return book

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
    def __init__(self):
        self.name = dt["name"]
        self.address = dt["address"]  # Адрес магазина.
        self.inventory = Inventory()  # Инвентарь магазина.
        self.cash_register = CashRegister()  # Касса магазина.
        self.cash_register.total_sales = dt["cash_register"]
        self.employees = [Employee(employee["name"], employee["role"], employee["salary"]) for employee in
                          dt["employees"]]  # Сотрудники.
        # self.categories = [] # Категории книг.
        self.orders = [Order(
            Customer(order["customer"]["name"], order["customer"]["email"], order["customer"]["phone"]),
            [book for book in order["books"]], order["quantity"], order["total_price"]) for order in dt["orders"]]

    def add_employee(self):  # Метод для добавления сотрудника в магазин.
        name = input("Введите имя сотрудника  ")
        role = input("Введите должность сотрудника  ")
        salary = int(input("Введите зарплату сотрудника  "))
        employee = Employee(name, role, salary)
        dt["employees"].append(employee.to_json())
        dtb.write_db(dt)
        self.employees.append(employee)

    def del_employee(self):
        if len(dt["employees"]) == 0:
            print("Список сотрудников пуст")
            return
        name = input("Введите имя сотрудника, которого хотите уволить  ")
        flag = False
        for i in range(len(dt["employees"])):
            if name == dt["employees"][i]["name"]:
                flag = True
                dt["employees"].pop(i)
                dtb.write_db(dt)
                self.employees.pop(i)
                return
        if not flag:
            print("Сотрудник не найден")

    def change_employee_salary(self):
        name = input("Введите имя сотрудника, которому хотите изменить зарплату  ")

        for i in range(len(dt["employees"])):
            if dt["employees"][i]["name"] == name:
                salary = int(input("Введите новую зарплату  "))
                dt["employees"][i]["salary"] = salary
                dtb.write_db(dt)
                self.employees[i].salary = salary
                return
        return print("Такого сотрудника нет")

    @staticmethod
    def print_employees():
        print("---------------------------------------------------------------------------")
        for i in range(len(dt["employees"])):
            print(
                f"Сотрудник: {dt["employees"][i]["name"]}, Должность: {dt["employees"][i]["role"]}, Зарплата: "
                f"{dt["employees"][i]["salary"]} руб.")
        print("---------------------------------------------------------------------------")

    def add_order(self):  # Метод для добавления заказа.
        phone = input("Введите телефон покупателя  ")
        customer_name = input("Введите имя покупателя  ")
        email = input("Введите почту покупателя  ")

        customer = Customer(customer_name, email, phone)
        sum_quantity = 0
        summ = 0
        books = []
        quantity = int(input("Введите количество позиций в заказе  "))
        for i in range(quantity):
            print("---------------------------------------------------------------------------")
            book_title = input("Введите название книги  ")
            quantity1 = int(input("Введите количество книг  "))
            if (self.inventory.check_book(book_title)) and (
                    self.inventory.search__by_title_one(book_title).stock >= quantity1):
                for j in range(len(dt["inventory"]["books"])):
                    if dt["inventory"]["books"][j]["title"] == book_title:
                        dt["inventory"]["books"][j]["stock"] -= quantity1
                        dtb.write_db(dt)
                        if dt["inventory"]["books"][j]["stock"] == 0:
                            dt["inventory"]["books"].pop(j)
                            dtb.write_db(dt)

                books.append(book_title)
                sum_quantity += quantity1
                summ += self.inventory.search__by_title_one(book_title).price * quantity1
                print("---------------------------------------------------------------------------")

            else:
                print("Книги нет на складе")
                return
        self.cash_register.total_sales += summ
        dt["cash_register"] += summ
        order = Order(customer, books, sum_quantity, summ)
        dt["orders"].append(order.to_json())
        dtb.write_db(dt)

    @staticmethod
    def print_books():
        print("---------------------------------------------------------------------------")
        for i in range(len(dt["inventory"]["books"])):
            print(f"Книга: {dt["inventory"]["books"][i]["title"]}, Автор: {dt["inventory"]["books"][i]["author"]},"
                  f" Жанр: {dt["inventory"]["books"][i]["genre"]}, Цена: {dt["inventory"]["books"][i]["price"]} "
                  f"руб. Кол-во на складе: {dt["inventory"]["books"][i]["stock"]}")
        print("---------------------------------------------------------------------------")

    @staticmethod
    def print_cash_register():
        print("---------------------------------------------------------------------------")
        print("Выручка кассы:   ", dt["cash_register"])
        print("---------------------------------------------------------------------------")

    @staticmethod
    def print_orders():
        print("Заказы")
        print("---------------------------------------------------------------------------")
        for i in range(len(dt["orders"])):
            books = ""
            for j in range(len(dt["orders"][i]["books"])):

                books += dt["orders"][i]["books"][j]
                if j + 1 != len(dt["orders"][i]["books"]):
                    books += ",   "

            print(f"Покупатель:  {dt["orders"][i]["customer"]["name"]}   {dt["orders"][i]["customer"]["email"]}    "
                  f"{dt["orders"][i]["customer"]["phone"]}   \nЗаказанные книги:   {books}\nКол-во книг:    "
                  f"{dt["orders"][i]["quantity"]}\nСумма заказа:   "
                  f"{dt["orders"][i]["total_price"]}\nСтатус заказа:   "
                  f"{dt["orders"][i]["status"]}")
            print("---------------------------------------------------------------------------")

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
            "cash_register": self.cash_register.get_total_sales(),
            "employees": [employee.to_json() for employee in self.employees],
            # "categories": self.categories,
            "orders": [order.to_json() for order in self.orders]
        }


dt = DataBase(PATH).dt
dtb = DataBase(PATH)

store = Store()
value = 1
while value != 0:
    print("Выберете действие:\n1 - Добавить книгу\n2 - Удалить книгу\n3 - Изменить количество книг"
          "\n4 - Добавить сотрудника\n5 - Удалить сотрудника\n6 - Изменить зарплату сотрудника\n7 - Создать заказ"
          "\n8 - Вывести книги\n9 - Вывести сотрудников\n10 - Вывести выручку\n11 - Вывести заказы\n0 - Выход\n")
    value = int(input())
    if value == 1:
        store.inventory.add_book()
    if value == 2:
        store.inventory.remove_book()
    if value == 3:
        store.inventory.change_stock()
    if value == 4:
        store.add_employee()
    if value == 5:
        store.del_employee()
    if value == 6:
        store.change_employee_salary()
    if value == 7:
        store.add_order()
    if value == 8:
        store.print_books()
    if value == 9:
        store.print_employees()
    if value == 10:
        store.print_cash_register()
    if value == 11:
        store.print_orders()
