def foo(n):

    def countdown(number):
        #  функция-генератор простых чисел
            for a in range(2, number):
                for b in range(2, a):
                    if a % b == 0:
                        break
                else:
                    yield a
                    #  Возврат простого числа

    for number in range(2, n):
        #  Перебор натуральных чисел
        c = countdown(number)
        #  Если добавить к number единицу в ответе появятся простые числа
        #  в ответ их не добавил т.к. в задание сказано
        #  разложить на простые множители
        local_result = number
        answer = []
        while True:
            #  цикл перебора простых чисел
            try:
                #  проверка на исключение остановки итерации
                while local_result != 1:
                    #  Цикл поиска простых множителей
                    #  получаем след. простое число
                    delim = c.__next__()
                    flag = True
                    while flag:
                        #  цикл делит на простое число до тех пор
                        #  пока остаток 0
                        if local_result % delim == 0:
                            local_result /= delim
                            answer.append(delim)
                        else:
                            flag = False
                else:
                    if len(answer) > 0:
                        print("число {} множители {}".
                              format(number, answer))
                    break
            except StopIteration:
                break


if __name__ == '__main__':
    foo(55)
