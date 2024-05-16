from database import Database


class TeacherCRUD:
    def __init__(self, uri, user, password) -> None:
        self._db = Database(uri, user, password)

    def create(self, name, ano_nasc, cpf):
        query = "CREATE(:Teacher{name: $name, ano_nasc: $ano_nasc, cpf: $cpf});"
        parameters = {
            "name": name,
            "ano_nasc": ano_nasc,
            "cpf": cpf
        }
        self._db.execute_query(query, parameters)

    def read(self, name):
        query = "MATCH (t:Teacher {name: $name}) RETURN t;"
        parameters = {
            "name": name,
        }

        result = self._db.execute_query(query, parameters)

        if result:
            return {
                'name': result[0]['t']['name'],
                'ano_nasc': result[0]['t']['ano_nasc'],
                'cpf': result[0]['t']['cpf']
            }
        else:
            return None

    def update(self, name, newCpf):
        query = "MATCH (t:Teacher {name: $name}) SET t.cpf = $newCpf RETURN t;"
        parameters = {
            "name": name,
            "newCpf": newCpf
        }

        result = self._db.execute_query(query, parameters)

        if result:
            return {
                'name': result[0]['t']['name'],
                'cpf': result[0]['t']['cpf']
            }
        else:
            return None

    def delete(self, name):
        query = "MATCH (t:Teacher {name: $name}) DETACH DELETE t;"
        parameters = {
            "name": name,
        }

        self._db.execute_query(query, parameters)

    def close(self):
        self._db.close()
        print('Conexão Encerrada')


if __name__ == '__main__':
    teacherCRUD = TeacherCRUD(
        'neo4j+s://54f4fa39.databases.neo4j.io',
        'neo4j',
        'mXNfxrDccsf4jixvUl2c7x5k51B711__j2ZXQkNB_0Q'
    )

    teacherCRUD.create(
        name='Chris Lima',
        ano_nasc=1956,
        cpf='189.052.396-66'
    )

    print(teacherCRUD.read('Chris Lima'))

    teacherCRUD.update('Chris Lima', "162.052.777-77")

    print(teacherCRUD.read('Chris Lima'))

    teacherCRUD.close()