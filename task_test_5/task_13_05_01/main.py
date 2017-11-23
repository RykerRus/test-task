# Программирование на языке высокого уровня (Python).
# Задание task_13_05_01. Вариант !!!
#
# Выполнила: Дарья Миляева
# Группа: !!!
# E-mail: !!!

import sys
from book_parser import BookParser

if __name__ == "__main__":
    try:
        if (len(sys.argv) == 2):
            book_parser = BookParser(sys.argv[1])
            print("Получение информации из файла...")
            book_parser.parse()
            book_parser.save(sys.argv[1])
            print("Результат сохранен!")
        else:
            result_path = input("Введите путь для сохранения результата: ")
            book_parser = BookParser(result_path)
            print("Получение информации из файла...")
            book_parser.parse()
            book_parser.save(result_path)
            print("\n", book_parser, "\n")
            print("Результат сохранен!")
    except Exception as err:
        raise err
        print("Во время работы программы произошла ошибка - {}!"
              .format(Exception))
