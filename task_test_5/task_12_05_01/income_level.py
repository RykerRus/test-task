# Программирование на языке высокого уровня (Python).
# Задание task_12_05_01. Вариант !!!
#
# Выполнил: Фамилия И.О.
# Группа: !!!
# E-mail: !!!
import csv
import re
import matplotlib.pyplot as plt


class income_level:
    def __init__(self):
        self._data = []
        self._data2 = []
        self._name_okrg = ["Центральный", "Северо-Западный", "Южный",
                           "Северный-Кавказкий", "Приволжский",
                           "Уральский", "Сибирский", "Дальневосточный",
                           "Крымский"]

    def load(self):
        with open("data_2017-12-27.csv", "r", encoding="utf-8") as fh:
            r = list(csv.reader(fh))
        sravnenie = None
        index = -1
        for a in r[1:]:
                b = a[0].split(";")
                if b[0] == "Северо-Кавказский федеральный округ":
                    self._data2.append((b[1], int(b[2])))
                if b[0] != sravnenie:
                    self._data.append(["", 0, 0])
                    index += 1
                if self._data[index][0] is "":
                    self._data[index][0] = b[0]
                self._data[index][1] += 1
                self._data[index][2] += (int(b[2]))
                sravnenie = self._data[index][0]

    def _make_plot(self):
        """Генерирует изображение, не отображая его.

        Изображение должно включать несколько диаграмм по горизонтали,
        количество которых равно длине 'self._data'.

        Если 'self._data' не содержит данных, возбудить AssertionError.

        Длина оси OX для каждой диаграммы должна быть вдвое больше
        значения точки безубыточности.

        Результат:
          - fig: matplotlib.figure.Figure.
        """
        if len(self._data) == 0:
            raise AssertionError
        else:
            d = self._data
            fig, ax = plt.subplots()
            fig1, ax1 = plt.subplots()
            values = list()
            labels = list()
            for i in range(len(d)):
                labels.append(self._name_okrg[i] + " " +
                              str(int((d[i][2] / d[i][1]))))
                values.append(d[i][2] / d[i][1])
            size = [x[1] for x in self._data2]
            nums = [x + 1 for x in range(len(size))]

            tick_label = [x for x in range(len(size))]
            ax1.set_ylabel("уровень доходов в федеральных округах")
            ax1.bar(nums, size, tick_label=tick_label, width=0.5,
                    color="#a500ff")
            # Смещение оси и легенды
            ax.pie(values, labels=labels, autopct="%.1f%%", radius=1.2)
            ax.set_aspect("equal")
            fig1.tight_layout()
            return fig

    def show_plot(self):
        """Создать изображение и показать его на экране."""
        self._make_plot()
        plt.show()
