from simple_cli import SimpleCLI
from User import User
from Task import Task
from Task_DAO import TaskDAO


class TaskCLI(SimpleCLI):
    def __init__(self, task_dao: TaskDAO, user: User):
        super().__init__()
        self.user = user
        self.task_dao = task_dao
        self.add_command("criar", self.create)
        self.add_command("update", self.update)
        self.add_command("delete", self.delete)
        self.add_command("readOne", self.readOne)
        self.add_command("readAll", self.readAll)

    def create(self):
        titulo = input("Titulo: ")
        descricao = input("Descricao: ")
        data = input("Data: ")

        task = Task(self.user, titulo, descricao, data, False)

        self.task_dao.create_task(task)

    def readOne(self):
        titulo = input("Titulo da task a ser lida: ")
        res = self.task_dao.get_by_name(titulo, self.user)

        print(f"Titulo: {res["titulo"]}\nDescricao: {res["descricao"]}\nData: {res["data"]}\nDone: {res["done"]}\n")
    
    def readAll(self):
        response = self.task_dao.readAll(self.user)

        for res in response:
            print(f"Titulo: {res["titulo"]}\nDescricao: {res["descricao"]}\nData: {res["data"]}\nDone: {res["done"]}\n")


    def update(self):
        titulo = input("Titulo da task a ser atualizada: ")
        print("(deixar vazio para manter o valor antigo)")
        novo_titulo = input("Titulo: ")
        descricao = input("Descricao: ")
        data = input("Data: ")
        done = input("Done: ")

        res = self.task_dao.get_by_name(titulo, self.user)

        task = Task(self.user, res["titulo"], res["descricao"], res["data"], res["done"])

        id = res["_id"]

        if (novo_titulo != ""):
            task.titulo = novo_titulo

        if (descricao != ""):
            task.descricao = descricao
            
        if (data != ""):
            task.data = data
            
        if (done != ""):
            task.done = done

        self.task_dao.update_task(id, task)

    def delete(self):
        titulo = input("Titulo da task a ser deletada: ")

        res = self.task_dao.get_by_name(titulo, self.user)

        id = res["_id"]

        self.task_dao.delete_task(id)


    def run(self):
        print("Bem-vindo ao CLI das tasks!")
        super().run()