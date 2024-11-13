from main import dt


class CashRegister:  # Кассовый аппарат
    def __init__(self):
        self.total_sales = dt["cash_register"]  # Выручка

    def process_payment(self, amount: int):  # Метод для обработки платежа
        self.total_sales += amount
        dt["cash_register"] += amount

    def get_total_sales(self):  # Метод для получения общей суммы всех продаж, сделанных через кассу магазина.
        return self.total_sales

    def to_json(self):  # Метод для записи в полей класса в файл json
        return {
            "total_sales": self.total_sales
        }
