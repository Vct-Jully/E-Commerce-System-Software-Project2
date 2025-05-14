from abc import ABC, abstractmethod

class Usuario(ABC):
    def __init__(self, usuario, senha, nome=None, email=None):
        self.usuario = usuario
        self.senha = senha
        self.nome = nome
        self.email = email
        self.enderecos = []

    def autenticar(self, usuario, senha):
        return self.usuario == usuario and self.senha == senha

    @abstractmethod
    def menu(self):
        pass

    def gerenciar_perfil(self):
        # Implementação do gerenciamento de perfil
        pass


class Administrador(Usuario):
    def menu(self):
        # Será implementado no controller
        pass


class Cliente(Usuario):
    def __init__(self, usuario, senha):
        super().__init__(usuario, senha)
        self.carrinho = []
    def view_orders(self):
        from models.order import OrderManager
        return OrderManager.get_user_orders(self.usuario)

    def menu(self):
        # Será implementado no controller
        pass