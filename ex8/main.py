from database import Database
from ex8.game_database import GameDatabase

# não colocarei as senhas aqui, por segurança
db = Database("bolt://3.235.168.48:7687", "neo4j", "badge-aid-strips")
db.drop_all()

game_db = GameDatabase(db)

game_db.create_player("Zé")
game_db.create_player("Fufu")
game_db.create_player("Lano")

game_db.create_match("match1")
game_db.create_match("match2")
game_db.create_match("match3")

game_db.update_player("Fufu", "Fu")

game_db.insert_player_match("Zé", "match1", 10)
game_db.insert_player_match("Fu", "match1", 9)
game_db.insert_player_match("Lano", "match1", 8)
game_db.insert_player_match("Zé", "match2", 10)

game_db.delete_player("Fu")
game_db.delete_match("match3")

print("Players:")
print(game_db.get_players())
print("Matchs:")
print(game_db.get_matchs())

db.close()