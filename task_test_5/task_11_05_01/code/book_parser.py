import re


class BookParser:
    def __init__(self, source_path, result_path):
        if not(isinstance(source_path, str)
               or isinstance(source_path, str)):
            raise TypeError("пути к сохраненной веб-странице и к"
                            "выходному файлу должны быть строкой!")

        self._source_path = source_path
        self._result_path = result_path

    def __str__(self):
        return ("№ п/п Характеристика     Информация \n"
                "1     Название           {}\n"
                "2     Список Авторов     {}\n"
                "3     Цена               {} руб.\n"
                "4     ISBN               {}\n"
                "5     Издательство       {}\n"
                "6     Количество страниц {}\n"
                "7     Год выпуска        {}\n"
                .format(self._book_info["name"],
                        ", ".join(self._book_info["authors"]),
                        self._book_info["price"],
                        self._book_info["ISBN"],
                        self._book_info["publisher"],
                        self._book_info["pages"],
                        self._book_info["publishing_year"]))

    def parse(self):
        with open(self._source_path, encoding="windows-1251") as fh:
            data = fh.read()
            self._book_info = self._info_from_str(data)

            with open(self._result_path, "w", encoding="utf-8") as fh_2:
                fh_2.write(str(self))

    def _info_from_str(self, data):
        m = re.search(r"<title>Книга  &#171;(?P<name>\w+).*"
                      "title=\"все книги этого издательства\">"
                      "(?P<publisher>.+)</a>.*"
                      "Год издания:</td><td class=\"block1\">"
                      "(?P<publishing_year>\d+).*"
                      "Страниц:</td><td class=\"block1\">"
                      "(?P<pages>\d+).*"
                      "ISBN:</td><td class=\"block1\">"
                      "(?P<ISBN>\d{3}-\d{1}-\d{3}-\d{5}-\d{1}).*"
                      "title=\"все книги автора\">"
                      "(?P<authors>.+)"
                      " — все книги автора.*"
                      "Цена в интернет-магазине:</span><br/>"
                      "(?P<price>\d+).*", data, re.DOTALL)

        if not(m):
            raise ValueError("Не удалось прочитать данные из строки!")

        result = m.groupdict()
        result["authors"] = tuple(result["authors"].split(", "))
        result["price"] = float(result["price"])
        result["pages"] = int(result["pages"])
        result["publishing_year"] = int(result["publishing_year"])
        return result
