from abc import ABC, abstractmethod

# --- Classes originais (mantidas) ---
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
        pass

class Administrador(Usuario):
    def menu(self):
        pass  # Implementado no AdminController

class Cliente(Usuario):
    def __init__(self, usuario, senha, nome=None, email=None):
        super().__init__(usuario, senha, nome, email)
        self.carrinho = []

    def view_orders(self):
        from models.order import OrderManager
        return OrderManager.get_user_orders(self.usuario)

    def menu(self):
        pass  # Implementado no ClientController

# --- Factory Method (nova adição) ---
class UsuarioFactory:
    @staticmethod
    def criar_usuario(tipo, usuario, senha, nome=None, email=None):
        """Cria instâncias de usuário baseadas no tipo.
        
        Args:
            tipo (str): 'admin' ou 'cliente'
            usuario (str): Nome de usuário
            senha (str): Senha
            nome (str, optional): Nome completo. Defaults to None.
            email (str, optional): E-mail. Defaults to None.
        
        Returns:
            Usuario: Instância de Administrador ou Cliente
        
        Raises:
            ValueError: Se o tipo for inválido.
        """
        if tipo.lower() == "admin":
            return Administrador(usuario, senha, nome, email)
        elif tipo.lower() == "cliente":
            return Cliente(usuario, senha, nome, email)
        else:
            raise ValueError("Tipo de usuário inválido. Use 'admin' ou 'cliente'.")
