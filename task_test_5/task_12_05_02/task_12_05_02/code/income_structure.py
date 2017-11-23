import matplotlib.pyplot as plt
import numpy as np
import csv


class Diagrams:
    """Класс - конструктор, который строит диаграммы."""

    def __init__(self):
        self.data = []
        self.ss = []
        self.name = []

    def sort_only(self):
        """Сортируется список для 4-го округа."""
        n = 0
        for row in self.data:
            if row[0] == "Северо-Кавказский федеральный округ":
                self.ss.append(row)
                n += 1
        for i in self.ss:
            i.pop(0)
        return n

    @staticmethod
    def summa(lst1, lst2):
        """Сумма значений для построения диаграмм."""
        a = []
        for i in range(len(lst1)):
            a.append(lst1[i] + lst2[i])
        return a

    def prnt_diagram(self):
        """Вывод диаграмм."""
        n = self.sort_only()
        l_pr = []
        l_opl_tr = []
        l_soc = []
        l_sob = []
        l_other = []
        l_subject = []
        for i in self.ss:
            l_subject.append(i[0])
            l_pr.append(i[1])
            l_opl_tr.append(i[2])
            l_soc.append(i[3])
            l_sob.append(i[4])
            l_other.append(i[5])
        ind = np.arange(n)
        width = 0.4
        fig, ax = plt.subplots(ncols=1)
        fig.autofmt_xdate()
        fig.canvas.set_window_title("Доход")
        x1 = plt.bar(ind, l_pr, width)
        x2 = plt.bar(ind, l_opl_tr, width, bottom=l_pr)
        x3_bott = self.summa(l_pr, l_opl_tr)
        x3 = plt.bar(ind, l_soc, width, bottom=x3_bott)
        x4_bott = self.summa(x3_bott, l_soc)
        x4 = plt.bar(ind, l_sob, width, bottom=x4_bott)
        x5_bott = self.summa(x4_bott, l_sob)
        x5 = plt.bar(ind, l_other, width, bottom=x5_bott)
        plt.ylabel('%')
        ttl_1 = "Структура доходов по субъектам РФ:"
        ttl_2 = "Северо-Кавказский федеральный округ"
        ttl = ttl_1 + ttl_2
        plt.title(ttl)
        plt.xticks(ind, l_subject)
        plt.yticks(np.arange(0, 110, 10))
        plt.legend((x1[0], x2[0], x3[0], x4[0], x5[0]), self.name)
        plt.show()

    def load(self, filename):
        """Загрузка информации из CSV файла."""
        reader = csv.reader(open(filename, encoding="utf-8"), delimiter=',')
        for row in reader:
            self.data.append('. '.join(row).split(";"))
        self.name.append(self.data[0])
        self.name = self.name.pop(0)
        self.name.pop(0)
        self.name.pop(0)
        self.data.pop(0)
        for i in self.data:
            for j in range(2, 7):
                i[j] = float(i[j].replace(" ", ""))
