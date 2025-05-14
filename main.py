from controllers.auth_controller import AuthController
from controllers.admin_controller import AdminController
from controllers.client_controller import ClientController
from views.auth_view import AuthView
from models.user import Administrador  # Adicionando esta importação

def main():
    auth = AuthController()
    auth_view = AuthView()
    
    while True:
        opcao = auth_view.show_main_menu()

        if opcao == "1":  # Login
            usuario, senha = auth_view.get_login_credentials()
            user,status = auth.login(usuario, senha)
            
            if status == "success":
                user_type = "Administrador" if isinstance(user, Administrador) else "Cliente"
                auth_view.show_login_success(user_type, user.usuario)
                
                if isinstance(user, Administrador):
                    AdminController(user).menu()
                else:
                    ClientController(user).menu()
            elif status == "not_found":
                auth_view.show_login_failed()
                usuario, senha = auth_view.get_register_credentials()
            elif status == "wrong password":
                auth_view.show_wrong_password()
                senha = input('digite a senha novamente')
                user, status = auth.login(usuario, senha)
                
        elif opcao == "2":  # Cadastro
            usuario, senha = auth_view.get_register_credentials()
            auth.register(usuario, senha)
            auth_view.show_register_success()

        elif opcao == "3":  # Sair
            print("Saindo...")
            break

if __name__ == "__main__":
    main()