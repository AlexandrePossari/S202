from database import Database
from bson.objectid import ObjectId

from projetoLab.Task import Task


class TaskDAO:
    def __init__(self, database: str, collection: str) -> None:
        self.db = Database(database, collection)

    def create_task(self, task: Task):
        try:
            res = self.db.collection.insert_one(task.get_dict())
            print(f"Task criado com o id: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"Ocorreu um erro na criação do Task: {e}")
            return None

    def read_task_by_id(self, id: str):
        try:
            res = self.db.collection.find_one({"_id": ObjectId(id)})
            return res
        except Exception as e:
            print(f"Ocorreu um erro buscando task: {e}")
            return None


    def update_task(self, id: str, task: Task):
        try:
            res = self.db.collection.update_one(
                {"_id": ObjectId(id)}, {"$set": task.get_dict()})
            print("Task atualizado!")
            return res.modified_count
        except Exception as e:
            print(f"Um erro ocorreu atualizando o Task: {e}")
            return None

    def delete_task(self, id: str):
        try:
            res = self.db.collection.delete_one({"_id": ObjectId(id)})
            print(f"Task deletado!")
            return res.deleted_count
        except Exception as e:
            print(f"Ocorreu um erro ao excluir um Task: {e}")
            return None