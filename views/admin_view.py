class AdminView:
    @staticmethod
    def show_menu():
        print("\n=== Menu de Administração ===")
        print("1 - Adicionar Produto")
        print("2 - Editar Produto")
        print("3 - Remover Produto")
        print("4 - Gerenciar Descontos")
        print("5 - Logout")
        return input("Escolha uma opção: ")

    @staticmethod
    def show_products(products):
        print("\nLista de Produtos:")
        for i, p in enumerate(products, start=1):
            print(f"{i} - Nome: {p['nome']}, Preço: R${p['preco']}")

    @staticmethod
    def get_product_info():
        nome = input("Digite o nome do produto: ")
        preco = float(input("Digite o preço do produto: R$"))
        return nome, preco

    # Outros métodos relacionados à visualização do admin