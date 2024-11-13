class Customer:  # Покупатель
    def __init__(self, name: str, email: str, phone: str):
        self.name = name  # имя покупателя.
        self.email = email  # электронная почта.
        self.phone = phone  # номер телефона.

    def __str__(self):
        return f"Покупатель: {self.name}, Email: {self.email}, Телефон: {self.phone}"

    def to_json(self):  # Метод для записи в полей класса в файл json
        return {
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            # "orders": self.orders_js
        }
