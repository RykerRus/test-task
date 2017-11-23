from time_collection import TimeCollection
from custom_time import Time

if __name__ == "__main__":
    time1 = Time.from_string(input("Введите 1-е время в формате -"
                                   " \"00:00:00\",\n\"00:00:00.000000\","
                                   "\n\"00:00:00.000000 UTC+3:0\": "))
    time2 = Time.from_string(input("Введите 2-е время в формате -"
                                   " \"00:00:00\",\n\"00:00:00.000000\","
                                   "\n\"00:00:00.000000 UTC+3:0\": "))
    time_collection = TimeCollection(time1, time2)
    print("TimeCollection \n", time_collection)

    time3 = Time.from_string(input("Введите 3-е время в формате -"
                                   " \"00:00:00\",\n\"00:00:00.000000\","
                                   "\n\"00:00:00.000000 UTC+3:0\": "))
    time_collection.add(time3)
    print("TimeCollection \n", time_collection)

    index = int(input("Введите число от 0 до 2 для удаления элемента из"
                      " коллекции: "))
    print("Элемент для удаления", time_collection[index])
    time_collection.remove(index)
    print("TimeCollection \n", time_collection)

    filename = input("Введите имя файла для сохранения коллекции: ")

    time_collection.save(filename)
    print("Файл успешно сохранен!")
    time_collection.load(filename)
    print("Файл успешно загружен!")
    print("TimeCollection \n", time_collection)
