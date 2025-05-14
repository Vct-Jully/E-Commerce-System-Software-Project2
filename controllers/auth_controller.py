from models.user import Administrador, Cliente
from views.auth_view import AuthView
class AuthController:
    def __init__(self):
        self.admins = [Administrador("admin", "admin123")]
        self.users = []

    def user_exists(self, username):
        return(any(u.usuario == username for u in self.admins) or any(u.usuario == username for u in self.users))

    def login(self, usuario, senha):

        user = None
        for admin in self.admins:
            if admin.usuario == usuario:
                user = admin
                break

        if not user:
            for u in self.users:
                if u.usuario == usuario:
                    user = u
                    break

        if not user:
            return None, "not_found"

        if not user.autenticar(usuario,senha):
            return None, "wrong_password"

        return user, "sucess"

    def register(self, usuario, senha):
        self.users.append(Cliente(usuario, senha))
        return self.users[-1]