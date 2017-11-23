import datetime
import re
from algorithm import Algorithm


class Game:
    DATE_FORMAT = "%d.%m.%Y %H:%M:%S"

    def __init__(self):
        self._attempts = 0

    def start(self):
        self._starting_time = datetime.datetime.today()

        print(
            "Добро пожаловать в игру 'Угадай число'!\n"
            "Время начала игры: {}\n\n"
            "Правила: вы загадываете любое число, я отгадываю.\n"
            .format(self._starting_time.strftime(self.DATE_FORMAT))
        )
        input("Загадайте число, затем нажмите Enter.\n")

        user_range = input("Введите через пробел границы"
                           " интервала, в котором находится"
                           " ваше число: ").split(" ")
        self._guess_range = range(*list(map(int, user_range)))
        lst = list(self._guess_range)
        lst.append(lst[-1] + 1)
        self._algorithm = Algorithm(lst)

        print("Теперь я попытаюсь отгадать ваше число. Если я сделаю"
              " это, введите '+' или 'да', в противном случае введите"
              " что-либо другое.\n")

        while (True):
            number = self._algorithm.get_number()

            if (number is None):
                print("Я перебрал все числа из заданного диапазона,"
                      " возможно вы ошиблись в ответе. Конец игры.")
                self._finish()
                break

            self._attempts += 1
            answer = input("Вы загадали число {}? - ".format(number))

            if ((answer == "+") or (answer == "да")):
                self._finish()
                break

    def _finish(self):
        self._finishing_time = datetime.datetime.today()
        self._log()

        print("\nИгра закончена.\n"
              "Время окончания: {}\n"
              "Количество попыток: {}"
              .format(self._finishing_time.strftime(self.DATE_FORMAT),
                      self._attempts))

    def _log(self):
        with open("log.txt", "a+", encoding="utf-8") as fh:
            fh.seek(0)
            data = fh.read()
            m = re.findall(r"Игра №\d+", data)
            number = len(m) + 1

            fh.write("Игра №{}\n"
                     "  Начало игры: {}\n"
                     "  Конец игры: {}\n"
                     "  Количество попыток: {}\n"
                     .format(number,
                             self._starting_time.strftime(self.DATE_FORMAT),
                             self._finishing_time.strftime(self.DATE_FORMAT),
                             self._attempts))
