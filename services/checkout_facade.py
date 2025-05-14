from services.payment_strategy import PaymentContext, CreditCardPayment, PixPayment

class CheckoutFacade:
    def __init__(self, carrinho, usuario):
        self.carrinho = carrinho
        self.usuario = usuario

    def finalizar_compra(self, metodo_pagamento):
        if not self._validar_estoque():
            return False, "Sem estoque para alguns itens."
        
        total = self._calcular_total()
        if self._processar_pagamento(metodo_pagamento, total):
            self._gerar_pedido()
            return True, "Compra finalizada!"
        return False, "Pagamento falhou."

    def _validar_estoque(self):
        # Simulação: sempre há estoque
        return True

    def _calcular_total(self):
        return sum(item['preco'] for item in self.carrinho)

    def _processar_pagamento(self, metodo, total):
        if metodo == "Cartão":
            strategy = CreditCardPayment()
        elif metodo == "Pix":
            strategy = PixPayment()
        else:
            return False
        
        context = PaymentContext(strategy)
        return context.execute_payment(total)

    def _gerar_pedido(self):
        from models.order import OrderManager
        OrderManager.create_order(self.usuario, self.carrinho, "Cartão", "Endereço padrão")
