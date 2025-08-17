class Account:
    def __init__(self, bank_name, card_holder, balance = 0):
        self._bank_name = bank_name
        self._card_holder = card_holder
        self._balance = balance

    def add (self, amount):
        if self._can_add(amount):
            self._balance += amount

    def _can_add(self, amount):
        return True

    def pay(self, amount):
        if self._can_pay(amount):
            self._balance -= amount

    def _can_pay(self, amount):
        return amount < self._balance

    def show(self):
        print(f'На счету {self._card_holder} есть {self._balance}')

class CreditAccount(Account):
    def __init__(self, bank_name, card_holder, credit_limit):
        super().__init__(bank_name, card_holder)
        self.credit_limit = -credit_limit

    def _can_add(self, amount):
        return self._balance + amount < 0

    def _can_pay(self, amount):
        return self._balance - amount >= self.credit_limit

    def show(self):
        print(f'На кредитном счету {self._card_holder} кредитный лимит{self.credit_limit} доступно {self._balance}')


account = CreditAccount('Beta-Bank', 'Stas Konstantinov', 300000)
account.pay(100000)
account.show()
account.add(200000)
account.show()
account.pay(500000)
account.show()
account.pay(50000)
account.show()