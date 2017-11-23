spisok = [1, 2, 3, 4, 5, 6, 7, 8] # O(1)
result = []  # O(1)
i = len(spisok) // 2   # O(1) = O(1) + O(1)
for a in spisok:# O(N) = O(N/2) т.к. всегда выходит на середине цикла
    result.append(a)  # O(1)
    if i is 0 or a is spisok[-1]: # O(1) = O(1) + O(1) + O(1) + O(1)
        break
    result.append(spisok.pop())  # O(1) = O(1) + O(1)
    i -= 1 # Q(1)
# итоговая алгоритма O(N)
print(result)
