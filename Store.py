from main import dt, dtb
from Inventory import Inventory
from Customer import Customer
from CashRegister import CashRegister
from Employee import Employee
from Order import Order
from Book import Book


class Store:  # Класс магазин
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
        salary = self.__get_salary()
        employee = Employee(name, role, salary)
        dt["employees"].append(employee.to_json())
        dtb.write_db(dt)
        self.employees.append(employee)

    def del_employee(self):  # Метод для увольнения сотрудника
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

    def change_employee_salary(self):  # Метод для изменения зарплаты сотрудника
        name = input("Введите имя сотрудника, которому хотите изменить зарплату  ")

        for i in range(len(dt["employees"])):
            if dt["employees"][i]["name"] == name:
                salary = self.__get_salary()
                dt["employees"][i]["salary"] = salary
                dtb.write_db(dt)
                self.employees[i].salary = salary
                return
        return print("Такого сотрудника нет")

    def __get_salary(self):  # Метод для обработки ошибки при получении зарплаты сотрудника
        try:
            salary = int(input("Введите новую зарплату  "))
            if not salary > 0:
                raise DataFormatError
            else:
                return salary
        except (DataFormatError, ValueError):
            print("Данные введены неверно! Попробуйте еще раз")
            return self.__get_salary()

    @staticmethod
    def print_employees():  # Метод для вывода сотрудников на экран
        print("---------------------------------------------------------------------------")
        for i in range(len(dt["employees"])):
            print(
                f"Сотрудник: {dt["employees"][i]["name"]}, Должность: {dt["employees"][i]["role"]}, Зарплата: "
                f"{dt["employees"][i]["salary"]} руб.")
        print("---------------------------------------------------------------------------")

    def __get_number(self):  # Метод для обработки ошибок при получении номера телефона
        try:
            phone_number = input("Введите номер телефона: ")
            if len(phone_number) > 0:
                if not ((phone_number[0] == '8' and len(phone_number) == 11) or (
                        phone_number[0] == '+' and phone_number[1] == '7') and len(phone_number) == 12):
                    raise DataFormatError
                else:
                    return phone_number
        except DataFormatError:
            print("Данные введены неверно! Попробуйте еще раз")
            return self.__get_number()

    def __get_mail(self):  # Метод для обработки ошибки при получении почты
        try:
            mail = input("Введите почту: ")
            if (mail[-10:] != "@gmail.com") and (mail[-8:] != "@mail.ru") and (mail[-10:] != "@yandex.ru"):
                raise DataFormatError
            else:
                return mail
        except DataFormatError:
            print("Данные введены неверно! Попробуйте еще раз")
            return self.__get_mail()

    def __get_count(self):  # Метод для обработки ошибок при получении количества позиций в заказе
        try:
            count = int(input("Введите количество позиций в заказе: "))
            if not count > 0:
                raise DataFormatError
            else:
                return count
        except (DataFormatError, ValueError):
            print("Данные введены неверно! Попробуйте еще раз")
            return self.__get_count()

    def __get_quantity(self):  # Метод для обработки ошибок при получении количества книги
        try:
            quantity = int(input("Введите количество книг  "))
            if not quantity > 0:
                raise DataFormatError
            else:
                return quantity
        except (DataFormatError, ValueError):
            print("Данные введены неверно! Попробуйте еще раз")
            return self.__get_quantity()

    def add_order(self):  # Метод для добавления заказа.
        phone = self.__get_number()
        customer_name = input("Введите имя покупателя  ")
        email = self.__get_mail()

        customer = Customer(customer_name, email, phone)
        sum_quantity = 0
        summ = 0
        books = []
        quantity = self.__get_count()
        for i in range(quantity):
            print("---------------------------------------------------------------------------")
            book_title = input("Введите название книги  ")
            quantity1 = self.__get_quantity()
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
    def print_books():  # Вывод книг
        print("---------------------------------------------------------------------------")
        for i in range(len(dt["inventory"]["books"])):
            print(f"Книга: {dt["inventory"]["books"][i]["title"]}, Автор: {dt["inventory"]["books"][i]["author"]},"
                  f" Жанр: {dt["inventory"]["books"][i]["genre"]}, Цена: {dt["inventory"]["books"][i]["price"]} "
                  f"руб. Кол-во на складе: {dt["inventory"]["books"][i]["stock"]}")
        print("---------------------------------------------------------------------------")

    @staticmethod
    def print_cash_register():  # Вывод выручки кассы
        print("---------------------------------------------------------------------------")
        print("Выручка кассы:   ", dt["cash_register"])
        print("---------------------------------------------------------------------------")

    @staticmethod
    def print_orders():  # Вывод заказов
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

    def to_json(self):  # Метод для записи в полей класса в файл json
        return {
            "name": self.name,
            "address": self.address,
            "inventory": self.inventory.to_json(),
            "cash_register": self.cash_register.get_total_sales(),
            "employees": [employee.to_json() for employee in self.employees],
            # "categories": self.categories,
            "orders": [order.to_json() for order in self.orders]
        }


class DataFormatError(Exception):
    pass
