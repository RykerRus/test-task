# Программирование на языке высокого уровня (Python).
# Задание task_13_05_01. Вариант !!!
#
# Выполнил: Фамилия И.О.
# Группа: !!!
# E-mail: !!!

from bs4 import BeautifulSoup
import re
import requests

class BookParser:
    def __init__(self, filename):
        self._filename = filename
        self._data = ""
        self._dict = {}

    def __str__(self):
        return ("№ п/п Характеристика     Информация \n"
                "1     Название           {}\n"
                "2     Список Авторов     {}\n"
                "3     Цена               {} руб.\n"
                "4     ISBN               {}\n"
                "5     Издательство       {}\n"
                "6     Количество страниц {}\n"
                "7     Год выпуска        {}\n"
                .format(self._dict["name_book"],
                        self._dict["name_avtor"],
                        self._dict["price"],
                        self._dict["isbn"],
                        self._dict["izd"],
                        self._dict["count_str"],
                        self._dict["year"]))

    def parse(self):
        URL = "https://www.moscowbooks.ru/book/897144/"
        r = requests.get(URL)
        soup = BeautifulSoup(r.text, 'html.parser')
        self._dict["name_avtor"] = (soup.find('a', 'author-name')
                                    .find(text=True))
        self._dict["name_book"] = (soup.find('h1', 'page-header__title')
                                   .string.strip())
        self._dict["price"] = float(soup.find('div', 'book__price')
                                    .string.strip()[:-5])
        opisanie = soup.find('div', 'book__details-right')
        self._dict["isbn"] = (opisanie.find_all('dl')[5].
                              find('dt', 'book__details-value')
                              .string.strip())
        self._dict["count_str"] = int(opisanie.find_all('dl')[1].
                                      find('dt', 'book__details-value')
                                      .string.strip())
        opisanie = soup.find('div', 'book__details-left')
        self._dict["izd"] = (opisanie.find_all('dl')[0]
                             .find('dt', 'book__details-value')
                             .string.strip())
        self._dict["year"] = int(opisanie.find_all('dl')[1]
                                 .find('dt', 'book__details-value')
                                 .string.strip())

    def save(self, filename):
        try:
            fh = open(filename, "w", encoding="utf-8")
            fh.write(self.__str__())
        finally:
            if fh:
                fh.close()
