import json
import os
from DataBase import DataBase

PATH = "json.json"  # Путь к базе данных

dt = DataBase(PATH).dt
dtb = DataBase(PATH)

# Консольное приложение
if __name__ == "__main__":
    from Store import Store
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
