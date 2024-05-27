from projetoLab.Task import Corrida


class User:
    def __init__(self, email, senha) -> None:
        self.email = email
        self.senha = senha

    def get_dict(self) -> dict:
        return {
            "email": self.email,
            "senha": self.senha
        }