class Order:
    def __init__(self, user, items, total, payment_method, shipping_address):
        self.user = user
        self.items = items
        self.total = total
        self.payment_method = payment_method
        self.shipping_address = shipping_address
        self.status = "Processando"  # Pode ser: Processando, Enviado, Entregue, Cancelado

    def update_status(self, new_status):
        self.status = new_status


# Lista para armazenar todos os pedidos
orders = []

class OrderManager:
    @staticmethod
    def create_order(user, cart, payment_method, shipping_address):
        total = sum(item['preco'] for item in cart)
        order = Order(user.usuario, cart.copy(), total, payment_method, shipping_address)
        orders.append(order)
        cart.clear()
        return order

    @staticmethod
    def get_user_orders(username):
        return [order for order in orders if order.user == username]