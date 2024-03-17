from database import Database
from helper.WriteAJson import writeAJson

db = Database(database="pokedex", collection="pokemons")
db.resetDatabase()


class Pokedex:
    def __init__(self, db: Database ):
        _db = Database

    def getPokemonsThatEvolve(self):
        return db.collection.find({"$or": [{"next_evolution": {"$exists": True}},{"prev_evolution": {"$exists": True}}]})

    def getPokemonByName(self, name):
        return db.collection.find({"name": name})
    
    def getLegendaryPokemon(self):
        return db.collection.find({"spawn_chance": 0})
    
    def getPokemonsByType(self, type):
        return db.collection.find({"type": type})
    
    def getPokemonsByWeakness(self, weakness):
        return db.collection.find({"weaknesses": weakness})



pokemonsThatEvolve = Pokedex(db)
pokemonsThatEvolve = pokemonsThatEvolve.getPokemonsThatEvolve()
writeAJson(pokemonsThatEvolve, "pokemonsThatEvolve")

pokemonByName = Pokedex(db)
pokemonByName = pokemonByName.getPokemonByName("Bulbasaur")
writeAJson(pokemonByName, "pokemonByName")

legendaryPokemon = Pokedex(db)
legendaryPokemon = legendaryPokemon.getLegendaryPokemon()
writeAJson(legendaryPokemon, "legendaryPokemon")

pokemonsByType = Pokedex(db)
pokemonsByType = pokemonsByType.getPokemonsByType("Grass")
writeAJson(pokemonsByType, "pokemonsByType")

pokemonsByWeakness = Pokedex(db)
pokemonsByWeakness = pokemonsByWeakness.getPokemonsByWeakness("Fire")
writeAJson(pokemonsByWeakness, "pokemonsByWeakness")