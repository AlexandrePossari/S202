from simple_cli import SimpleCLI
from User import User
from Task_DAO import TaskDAO
from task_cli import TaskCLI


class TaskCLI(SimpleCLI):
    def __init__(self, task_dao: TaskDAO):
        super().__init__()
        self.task_dao = task_dao
        self.add_command("criar", self.create)
        self.add_command("registra", self.register)
        self.add_command("completa", self.complete)
        self.add_command("busca", self.buscar)
        self.add_command("deleta", self.deleta)

    def run(self):
        print("Bem-vindo ao CLI das tasks!")
        super().run()