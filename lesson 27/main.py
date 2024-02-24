class Account:
    rate_of_ruble_for_dollar = 0.010805
    rate_of_ruble_for_euro = 0.010065

    def __init__(self, surname, number_of_bank_account, percentage_of_accrual, amount_of_rubles):
        self.__surname = surname
        self.__number_of_bank_account = number_of_bank_account
        self.__percentage_of_accrual = percentage_of_accrual
        self.__amount_of_rubles = amount_of_rubles
        print(f'Счёт #{self.__number_of_bank_account}, принадлежащий {self.__surname} был открыт.')
        self.information_about_bank_account()
    
    @classmethod
    def redact_rate_of_ruble_for_dollar(cls, new_rate_of_ruble_for_dollar):
        cls.rate_of_ruble_for_dollar = new_rate_of_ruble_for_dollar

    @classmethod
    def redact_rate_of_ruble_for_euro(cls, new_rate_of_ruble_for_euro):
        cls.rate_of_ruble_for_euro = new_rate_of_ruble_for_euro
    
    @staticmethod
    def __transform_ruble_for_dollar(amount_of_rubles):
        return Account.rate_of_ruble_for_dollar * amount_of_rubles

    @staticmethod
    def __transform_ruble_for_euro(amount_of_rubles):
        return Account.rate_of_ruble_for_euro * amount_of_rubles    

    def information_about_bank_account(self):
        print(f'''Информация от счёте:
            {'-' * 40}
            #{self.__number_of_bank_account}
            Владелец: {self.__surname}
            Текущий баланс: {self.__amount_of_rubles} RUB
            Проценты: {self.__percentage_of_accrual:.0%}
            {'-' * 40}
            Состояние счёта: {round(Account.__transform_ruble_for_dollar(self.__amount_of_rubles), 2)}
            Состояние счёта: {round(Account.__transform_ruble_for_euro(self.__amount_of_rubles), 2)}''')

my_account = Account('Губин', 1102, 0.04, 999999)
Account.redact_rate_of_ruble_for_dollar(0.0113)
Account.redact_rate_of_ruble_for_euro(0.0091)
print('\nКурс изменился.')
my_account.information_about_bank_account()