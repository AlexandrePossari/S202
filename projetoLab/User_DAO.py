from database import Database
from bson.objectid import ObjectId

from User import User


class UserDAO:
    def __init__(self, database: str, collection: str) -> None:
        self.db = Database(database, collection)

    def create_user(self, user: User):
        try:
            res = self.db.collection.insert_one(user.get_dict())
            print(f"User criado com o id: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"Ocorreu um erro na criação do User: {e}")
            return None

    def read_user_by_email_pass(self, email: str, password: str):
        try:
            res = self.db.collection.find_one({"email": email, "senha": password})
            return res
        except Exception as e:
            print(f"Ocorreu um erro buscando user: {e}")
            return None

    def read_user_by_id(self, id: str):
        try:
            res = self.db.collection.find_one({"_id": ObjectId(id)})
            return res
        except Exception as e:
            print(f"Ocorreu um erro buscando user: {e}")
            return None

    def update_user(self, id: str, user: User):
        try:
            res = self.db.collection.update_one(
                {"_id": ObjectId(id)}, {"$set": user.get_dict()})
            print("User atualizado!")
            return res.modified_count
        except Exception as e:
            print(f"Um erro ocorreu atualizando o User: {e}")
            return None

    def delete_user(self, id: str):
        try:
            res = self.db.collection.delete_one({"_id": ObjectId(id)})
            print(f"User deletado!")
            return res.deleted_count
        except Exception as e:
            print(f"Ocorreu um erro ao excluir um User: {e}")
            return None