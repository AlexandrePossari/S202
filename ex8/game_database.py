
class GameDatabase:
    def __init__(self, database):
        self.db = database

    def create_player(self, name):
        query = "CREATE (:Player {name: $name})"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)

    def create_match(self, name):
        query = "CREATE (:Match {name: $name})"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)

    def get_players(self):
        query = "MATCH (p:Player) RETURN p.name AS name"
        results = self.db.execute_query(query)
        return [result["name"] for result in results]


    def get_matchs(self):
        query = "MATCH (a:Aula)<-[:JOGA]-(p:Player) RETURN a.name AS name, p.name AS player_name"
        results = self.db.execute_query(query)
        return [(result["name"], result["player_name"]) for result in results]

    def update_player(self, old_name, new_name):
        query = "MATCH (p:Player {name: $old_name}) SET p.name = $new_name"
        parameters = {"old_name": old_name, "new_name": new_name}
        self.db.execute_query(query, parameters)
    
    def insert_player_match(self, player_name, aula_name, pontuacao):
        query = "MATCH (a:Player {name: $player_name}) MATCH (b:Aula {name: $aula_name}) CREATE (a)-[:JOGA {pontuacao:"+pontuacao+"}]->(b)"
        parameters = {"player_name": player_name, "aula_name": aula_name}
        self.db.execute_query(query, parameters)

    def delete_player(self, name):
        query = "MATCH (p:Player {name: $name}) DETACH DELETE p"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)

    def delete_match(self, name):
        query = "MATCH (a:Match {name: $name}) DETACH DELETE a"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)
