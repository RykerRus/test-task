from custom_time import Time

if __name__ == "__main__":
    time1 = Time.from_string(input("Введите 1-е время в формате"
                                   " \"00:00:00\",\n\"00:00:00.000000\","
                                   "\n\"00:00:00.000000 UTC+3:0\": "))
    time2 = Time.from_string(input("Введите 2-е время в формате"
                                   " \"00:00:00\",\n\"00:00:00.000000\","
                                   "\n\"00:00:00.000000 UTC+3:0\": "))
    print("Time min -- {}".format(time1.min))
    print("Time max -- {}".format(time1.max))
    print("Time resolution -- {}".format(time1.resolution))
    print("Time {} hour -- {}".format(time1, time1.hour))
    print("Time {} minute -- {}".format(time1, time1.minute))
    print("Time {} second -- {}".format(time1, time1.second))
    print("Time {} microsecond -- {}".format(time1, time1.microsecond))
    print("Time {} tzinfo -- {}".format(time1, time1.tzinfo))
    print("bool {} -- {}".format(time1, bool(time1)))
    print("isoformat {} -- {}".format(time1, time1.isoformat()))
    print("utcoffset {} -- {}".format(time1, time1.utcoffset()))
    print("tzname {} -- {}".format(time1, time1.tzname()))
    print("{} == {} -- {}".format(time1, time2, time1 == time2))
    print("{} != {} -- {}".format(time1, time2, time1 != time2))
    print("{} > {} -- {}".format(time1, time2, time1 > time2))
    print("{} < {} -- {}".format(time1, time2, time1 < time2))
    print("{} >= {} -- {}".format(time1, time2, time1 >= time2))
    print("{} <= {} -- {}".format(time1, time2, time1 <= time2))
    filename = input("Введите имя файла: ")
    time1.save(filename)
    print("Время сохранено!")
    print("Время загружено - {}".format(Time().load(filename)))
