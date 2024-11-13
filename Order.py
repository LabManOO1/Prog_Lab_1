from Customer import Customer


class Order:  # Заказ
    def __init__(self, customer: Customer, books: list, quantity: int, total_price: int):
        self.customer = customer  # покупатель, который сделал заказ.
        self.book = books  # список заказанных книг
        self.quantity = quantity  # количество заказанных книг.
        self.total_price = total_price
        self.status = "in progress"

    def complete_order(self):  # Метод для завершения заказа.
        self.status = 'completed'

    def cancel_order(self):  # Метод для отмены заказа.
        self.status = 'cancelled'

    def to_json(self):  # Метод для записи в полей класса в файл json
        return {
            "customer": self.customer.to_json(),
            "books": self.book,
            "quantity": self.quantity,
            "total_price": self.total_price,
            "status": self.status
        }
