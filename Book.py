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

    def to_json(self):  # Метод для записи в полей класса в файл json
        return {
            "title": self.title,
            "author": self.author,
            "genre": self.genre,
            "price": self.price,
            "stock": self.stock
        }
