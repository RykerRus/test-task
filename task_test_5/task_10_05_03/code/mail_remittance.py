from remittance import Remittance


class MailRemittance(Remittance):
    def __init__(self, money, receiver_postcode, sender_postcode):
        if not (isinstance(receiver_postcode, int)):
            raise TypeError("Индекс получателя должен быть int!")
        if not (isinstance(sender_postcode, int)):
            raise TypeError("Индекс отправителя должен быть int!")

        super().__init__(money)
        self.__receiver_postcode = receiver_postcode
        self.__sender_postcode = sender_postcode

    def _check_postcode(self, postcode):
        # Проверка правильности почтового индекса

        return True

    def execute(self):
        assert self._check_postcode(self.__receiver_postcode), \
            "Индекс получателя неверен"
        assert self._check_postcode(self.__receiver_postcode),  \
            "Индекс отправилетя неверен"

        super().execute()
