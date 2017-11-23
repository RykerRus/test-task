import json
from functools import reduce
from custom_time import Time


class TimeCollection:
    def __init__(self, *items):
        self._data = []

        for item in items:
            self.add(item)

    def __str__(self):
        return reduce(lambda res, x: res + "\n{}".format(x),
                      self._data,
                      "Список элементов ({}):".format(len(self._data)))

    def __getitem__(self, index):
        if not(isinstance(index, int)):
            raise TypeError("index должен быть int!")
        return self._data[index]

    def add(self, value):
        if not(isinstance(value, Time)):
            raise TypeError("Допускает хранение только экземпляров"
                            " класса Time!")

        self._data.append(value)

    def remove(self, index):
        if not(isinstance(index, int)):
            raise TypeError("index должен быть int!")
        if not(0 <= index <= len(self._data)):
            raise ValueError("index вне диапазона!")

        del self._data[index]

    def save(self, filename):
        if not (isinstance(filename, str)):
            raise TypeError("Имя файла должно быть строкой!")

        with open("{}.json".format(filename), "w", encoding="utf-8") as fh:
            data = []
            for item in self._data:
                data.append(str(item))

            fh.write(json.dumps(data, ensure_ascii=False, indent=4))

    def load(self, filename):
        if not (isinstance(filename, str)):
            raise TypeError("Имя файла должно быть строкой!")

        with open("{}.json".format(filename), encoding="utf-8") as fh:
            lst = json.loads(fh.read())
            newData = []

            for item in lst:
                newData.append(Time.from_string(item))

            self._data = newData
