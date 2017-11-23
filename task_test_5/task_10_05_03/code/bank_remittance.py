from remittance import Remittance


class BankRemittance(Remittance):
    def __init__(self, money, receiver_account, sender_account):
        if not (isinstance(receiver_account, int)):
            raise TypeError("Номер счета получателя должен быть int!")
        if not (isinstance(sender_account, int)):
            raise TypeError("Номер счета отправителя должен быть int!")

        super().__init__(money)
        self.__receiver_account = receiver_account
        self.__sender_account = sender_account

    def _check_account_money(self):
        # Проверка наличия необходимых средств на счету
        return True

    def execute(self):
        assert self._check_account_money(), "Недостаточно денег на счету!"

        super().execute()
