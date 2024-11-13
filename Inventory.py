from Book import Book
from main import dt, dtb


class Inventory:  # Инвентарь
    def __init__(self):

        self.books = [Book(book["title"], book["author"], book["genre"], book["price"], book["stock"]) for book in
                      dt["inventory"]["books"]]  # пустой список, в который будут добавляться книги.

    def add_book(self):  # Метод для добавления книги в инвентарь магазина.

        if len(dt["inventory"]["books"]) == 0:
            title = input("Введите название книги  ")
            author = input("Введите автора книги  ")
            genre = input("Введите жанр книги  ")
            price = self.__get_price()
            stock = self.__get_stock()
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
                stock = self.__get_stock()
                dt["inventory"]["books"][i]["stock"] += stock
                dtb.write_db(dt)
                return
            else:
                genre = input("Введите жанр книги  ")
                price = self.__get_price()
                stock = self.__get_stock()
                book = Book(title, author, genre, price, stock)
                dt["inventory"]["books"].append(book.to_json())
                dtb.write_db(dt)

                self.books.append(book)
                return

    def __get_price(self):  # Метод для обработки ошибки при получении цены
        try:
            price = int(input("Введите цену книги  "))
            if not price > 0:
                raise DataFormatError
            else:
                return price
        except (DataFormatError, ValueError):
            print("Данные введены неверно! Попробуйте еще раз")
            return self.__get_price()

    def __get_stock(self):  # Метод для обработки ошибки при получении кол-ва книг
        try:
            stock = int(input("Введите кол-во книг, которое хотите добавить  "))
            if not stock > 0:
                raise DataFormatError
            else:
                return stock
        except (DataFormatError, ValueError):
            print("Данные введены неверно! Попробуйте еще раз")
            return self.__get_stock()

    def change_stock(self):  # Изменение количества книг
        name = input("Введите название книги, количество которой хотите изменить  ")
        stock = self.__get_stock()
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
                stock = self.__get_stock()

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

    def get_books(self):  # Метод, который возвращает список книг
        return self.books

    def check_book(self, book_title: str):  # Проверка на наличие книги
        for i in range(len(self.books)):
            if book_title == self.books[i].title:
                return True
        return False

    def search__by_title_one(self, title: str):  # Поиск книги по названию
        for book in self.books:
            if book.title == title:
                return book

    def list_books(self):  # Метод для получения списка всех книг в инвентаре магазина.

        return [str(book) for book in self.books]

    def search_by_title(self, title: str):  # Метод для поиска книг по названию.
        return [book for book in self.books if title.lower() in book.title.lower()]

    def search_by_author(self, author: str):  # Метод для поиска книг по автору.
        return [book for book in self.books if author.lower() in book.author.lower()]

    def to_json(self):  # Метод для записи в полей класса в файл json
        return {
            "books": [book.to_json() for book in self.books]
        }


class DataFormatError(Exception):
    pass
