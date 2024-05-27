from User import User

class Task:
    def __init__(self,  user: User, titulo, descricao, data) -> None:
        self.user = user
        self.titulo = titulo
        self.descricao = descricao
        self.data = data
