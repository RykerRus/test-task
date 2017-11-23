from bank_remittance import BankRemittance
from currency_remittance import CurrencyRemittance
from mail_remittance import MailRemittance


if __name__ == "__main__":
    print("1. Почтовый перевод")
    money = float(input("Введите кол-во денег: "))
    receiver_postcode = int(input("Введите почтовый индекс получателя: "))
    sender_postcode = int(input("Введите почтовый индекс отправителя: "))
    mail_remittance = MailRemittance(money, receiver_postcode,
                                      sender_postcode)
    mail_remittance.execute()

    print("2. Банковский перевод")
    money = float(input("Введите кол-во денег: "))
    receiver_account = int(input("Введите номер счёта получателя: "))
    sender_account = int(input("Введите номер счёта отправителя: "))
    bank_remittance = BankRemittance(money, receiver_account, sender_account)
    bank_remittance.execute()

    print("3. Валютный перевод")
    money = float(input("Введите кол-во денег: "))
    print("Поддерживаемая валюта: ", CurrencyRemittance.CURRENCY)
    currency_from = input("Введите название отправляемой валюты: ")
    currency_to = input("Введите название получаемой валюты: ")
    receiver_account = int(input("Введите номер счёта получателя: "))
    sender_account = int(input("Введите номер счёта отправителя: "))
    currency_remittance = CurrencyRemittance(money, receiver_account,
                                              sender_account, currency_from,
                                              currency_to)
    currency_remittance.execute()
