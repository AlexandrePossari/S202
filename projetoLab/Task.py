from User import User

class Task:
    def __init__(self,  user: User, titulo, descricao, data, done: bool) -> None:
        self.user = user
        self.titulo = titulo
        self.descricao = descricao
        self.data = data
        self.done = done

    def get_dict(self) -> dict:
        return {
            "titulo": self.titulo,
            "descricao": self.descricao,
            "data": self.data,
            "done": self.done,
            "user": self.user.get_dict()
        }