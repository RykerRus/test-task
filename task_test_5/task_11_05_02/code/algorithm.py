import math


class Algorithm:
    def __init__(self, array):
        if not(isinstance(array, list)):
            raise TypeError("Агрумент должен быть списком!")

        self._step = 0
        self._from_start = True
        self._array = array
        self._max_step = int(math.ceil(len(array) / 2))

    def get_number(self):
        if (self._check_step_limit()):
            return

        if (self._from_start):
            self._from_start = False
            return self._array[self._step]

        self._from_start = True
        number = self._array[len(self._array) - (self._step + 1)]
        self._step += 1

        return number

    def _check_step_limit(self):
        # Возвращает True, если достигнут максимальный шаг.

        if (len(self._array) == 2):
            if (self._step == 1):
                return True
        else:
            if ((self._step + 1 >= self._max_step)
               and (not self._from_start)):
                return True
