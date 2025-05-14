class ClientView:
    @staticmethod
    def show_menu():
        print("\n=== Menu do Cliente ===")
        print("1 - Ver Produtos")
        print("2 - Comprar ou Adicionar ao Carrinho")
        print("3 - Gerenciar Carrinho")
        print("4 - Gerenciar Perfil")
        print("5 - Avaliar Produto")
        print("6 - Logout")
        return input("Escolha uma opção: ")

    @staticmethod
    def show_products(products):
        print("\nLista de Produtos Disponíveis:")
        for i, p in enumerate(products, start=1):
            print(f"{i} - Nome: {p['nome']}, Preço: R${p['preco']}")
    
    @staticmethod
    def show_orders(orders):
        if not orders:
            print("Você não tem pedidos ainda.")
            return
    
        print("\n=== Seus Pedidos ===")
        for i, order in enumerate(orders, 1):
            print(f"\nPedido #{i}")
            print(f"Status: {order.status}")
            print(f"Total: R${order.total:.2f}")
            print("Itens:")
            for item in order.items:
                print(f"- {item['nome']} (R${item['preco']:.2f})")
        # Outros métodos relacionados à visualização do cliente