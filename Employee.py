class Employee:  # Сотрудник
    def __init__(self, name: str, role: str, salary: int):
        self.name = name  # имя сотрудника.
        self.role = role  # должность сотрудника
        self.salary = salary  # зарплата сотрудника.

    def receive_payment(self, amount: int):  # Метод для выплаты заработной платы сотруднику.
        self.salary += amount

    def __str__(self):
        return f"Сотрудник: {self.name}, Должность: {self.role}, Зарплата: {self.salary} руб."

    def to_json(self):  # Метод для записи в полей класса в файл json
        return {
            "name": self.name,
            "role": self.role,
            "salary": self.salary
        }
