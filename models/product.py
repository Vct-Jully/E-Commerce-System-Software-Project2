products = []
discounts = {}
product_reviews = {}

class Product:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    @staticmethod
    def add_product(nome, preco):
        products.append({"nome": nome, "preco": preco})

    @staticmethod
    def get_products(sort_by=None):
        if sort_by == "nome":
            return sorted(products, key=lambda x: x['nome'])
        elif sort_by == "preco":
            return sorted(products, key=lambda x: x['preco'])
        return products.copy()