from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Pagamento de R${amount} via Cartão de Crédito aprovado!")
        return True

class PixPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Pagamento de R${amount} via Pix realizado!")
        return True

class PaymentContext:
    def __init__(self, strategy):
        self.strategy = strategy

    def execute_payment(self, amount):
        return self.strategy.pay(amount)
