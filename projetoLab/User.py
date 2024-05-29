
class User:
    def __init__(self, nome, email, senha) -> None:
        self.nome = nome
        self.email = email
        self.senha = senha

    def get_dict(self) -> dict:
        return {
            "nome": self.nome,
            "email": self.email,
            "senha": self.senha
        }