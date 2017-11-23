#! -*- coding: utf-8 -*-


def divide(n, m):
    if m >= n:
        raise ValueError('M must be less then N!')
    dlina = n // m
    start = (n - (m * dlina)) // 2
    # n - (m * dlina) // 2 формула непокрытой части вектора
    result = []
    for a in range(m):
        result.append((start, start + dlina - 1))
        start += dlina
    return result

if __name__ == '__main__':
    n = int(input('Enter vector size N: '))
    m = int(input('Enter number of parts M: '))



    parts = divide(n, m)
    print("Начало вектора 0 конец {} элементов {}".format(n - 1, n))
    print(parts)
