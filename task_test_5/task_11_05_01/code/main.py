import sys
from book_parser import BookParser

if __name__ == "__main__":
    try:
        if (len(sys.argv) == 3):
            book_parser = BookParser(sys.argv[1], sys.argv[2])
            print("Получение информации из файла...")
            book_parser.parse()
            print("Результат сохранен!")
        else:
            source_path = input("Введите путь к html файлу: ")
            result_path = input("Введите путь для сохранения результата: ")
            book_parser = BookParser(source_path, result_path)
            print("Получение информации из файла...")
            book_parser.parse()
            print("Результат сохранен!")
    except Exception:
        print("Во время работы программы произошла ошибка - {}!"
              .format(Exception))
