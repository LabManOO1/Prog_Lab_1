import json
import os


class DataBase:  # Класс для работы с базой данных
    def __init__(self, path: str):
        if os.path.isfile(path):
            self.__path = path
            self.dt = self.db()

    def db(self):  # Открытие файла
        try:
            with open(self.__path, 'r') as jsfile:
                return json.load(jsfile)
        except FileNotFoundError:
            print("Невозможно открыть файл!")

    def write_db(self, dt: dict):  # Запись в файл
        with open(self.__path, 'w', encoding="utf-8") as jsfile:
            json.dump(dt, jsfile, indent=3)
