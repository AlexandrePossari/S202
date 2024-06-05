from simple_cli import SimpleCLI
from User_DAO import UserDAO
from User import User
from Task_DAO import TaskDAO
from task_cli import TaskCLI


class UserCLI(SimpleCLI):
    def __init__(self, user_Dao: UserDAO):
        super().__init__()
        self.user_Dao = user_Dao
        self.add_command("login", self.login)
        self.add_command("register", self.register_user)

    def register_user(self):
        nome = input("Nome: ")
        email = input("Email: ")
        senha = input("Senha: ")

        user = User(nome, email, senha)

        self.user_Dao.create_user(user)

    def login(self):
        email = input("Email: ")
        senha = input("Senha: ")

        res = self.user_Dao.read_user_by_email_pass(email, senha)

        if not res:
            print("Email ou senha incorreto")
            return
        
        user = User(res["nome"], res["email"], res["senha"])

        task_dao = TaskDAO('Projeto', 'Tasks')
        task_cli = TaskCLI(task_dao, user)
        task_cli.run()

    def run(self):
        print("Bem-vindo ao CLI do motorista!")
        super().run()