from models.product import Product
from views.admin_view import AdminView

class AdminController:
    def __init__(self, admin):
        self.admin = admin
        self.view = AdminView()

    def menu(self):
        while True:
            opcao = self.view.show_menu()

            if opcao == "1":
                nome, preco = self.view.get_product_info()
                Product.add_product(nome, preco)
                print(f"Produto {nome} adicionado!")

            elif opcao == "2":
                products = Product.get_products()
                self.view.show_products(products)
                # Implementar edição

            elif opcao == "4":
                print("Saindo do menu de administração...")
                break