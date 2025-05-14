from models.product import Product
from models.order import OrderManager
from views.client_view import ClientView

class ClientController:
    def __init__(self, client):
        self.client = client
        self.view = ClientView()

    def menu(self):
        while True:
            opcao = self.view.show_menu()

            if opcao == "1":  # Ver Produtos
                sort_option = input("Ordenar por (1-Nome, 2-Preço, Enter-Sem ordenação): ")
                products = Product.get_products("nome" if sort_option == "1" else "preco" if sort_option == "2" else None)
                self.view.show_products(products)

            elif opcao == "2":  # Comprar/Adicionar ao Carrinho
                products = Product.get_products()
                self.view.show_products(products)
                self.handle_purchase_or_add_to_cart(products)

            elif opcao == "3":  # Gerenciar Carrinho
                self.manage_cart()

            elif opcao == "4":  # Gerenciar Perfil
                self.client.gerenciar_perfil()

            elif opcao == "6":  # Logout
                print("Logout realizado.")
                break

    def handle_purchase_or_add_to_cart(self, products):
        # Implementação similar à função comprar_ou_adicionar do código original
        pass

    def manage_cart(self):
        # Implementação similar à função gerenciar_carrinho do código original
        pass

    def view_orders(self):
        user_orders = OrderManager.get_user_orders(self.client.usuario)
        if not user_orders:
            print("Você não tem pedidos ainda.")
            return
        
        print("\n=== Seus Pedidos ===")
        for i, order in enumerate(user_orders, 1):
            print(f"\nPedido #{i}")
            print(f"Status: {order.status}")
            print(f"Total: R${order.total:.2f}")
            print("Itens:")
            for item in order.items:
                print(f"- {item['nome']} (R${item['preco']:.2f})")