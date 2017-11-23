from bank_remittance import BankRemittance


class CurrencyRemittance(BankRemittance):
    CURRENCY = ["RUB", "EUR", "USD"]
    __currency_rate = {
        "RUB": 1,
        "EUR": 65,
        "USD": 60
    }

    def __init__(self, money, receiver_account, sender_account,
                 currency_from, currency_to):
        if not (isinstance(currency_from, str)):
            raise TypeError("Название валюты должо быть str!")
        if not (isinstance(currency_to, str)):
            raise TypeError("Название валюты должо быть str!")
        if not ((currency_from in self.CURRENCY)
                or (currency_from in self.CURRENCY)):
            raise ValueError("Данная валюта не поддерживается")
        super().__init__(money, receiver_account, sender_account)
        self._money["currency"] = currency_from
        self._currency_from = currency_from
        self._currency_to = currency_to

    def _convert_money(self):
        money = self._money["value"]

        if (self._currency_from != "RUB"):
            money *= self.__currency_rate[self._currency_from]

        if (self._currency_to != "RUB"):
            money /= self.__currency_rate[self._currency_to]

        self._money["value"] = round(money, 2)
        self._money["currency"] = self._currency_to

    def execute(self):
        self._convert_money()
        super().execute()
