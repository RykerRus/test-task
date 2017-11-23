class Remittance:
    MIN_VALUE = 0

    def __init__(self, money):
        if not (isinstance(money, float)):
            raise TypeError("Сумма перевода должна быть числом!")

        self._money = {}
        self._money["value"] = money
        self._money["currency"] = "RUB"

    def _check_money(self):
        return self._money["value"] > self.MIN_VALUE

    def execute(self):
        assert self._check_money(), "При выполнение перевода произошла ошибка"
        print("Перевод успешно выполнен!")
