class AuthView:
    @staticmethod
    def show_main_menu():
        print("\n=== Menu Principal ===")
        print("1 - Fazer Login")
        print("2 - Cadastrar Usuario")
        print("3 - Sair")
        select = input("Escolha uma opcao:\n ")
        return select

    @staticmethod
    def get_login_credentials():
        print("\n=== Login ===")
        usuario = None
        senha = None
        usuario = input("Usuário: ")
        senha = input("Senha: ")
        return usuario, senha

    @staticmethod
    def get_register_credentials():
        print("\n=== Cadastro ===")
        usuario = input("Novo usuário: ")
        senha = input("Senha: ")
        return usuario, senha

    @staticmethod
    def show_login_success(user_type, username):
        print(f"\nLogin bem-sucedido como {user_type}: {username}")

    @staticmethod
    def show_login_failed():
        print("\nUsuário ou senha incorretos!")

    @staticmethod
    def show_register_success():
        print("\nCadastro realizado com sucesso!")

    @staticmethod
    def show_user_not_found():
        print("Usuário Inexistente!")
        choice = input("Deseja se cadastrar? (S/N)").strip().upper()
        return choice == 'S'

    @staticmethod
    def show_wrong_password():
        print("\nSenha incorreta! Tente novamente:\n")

