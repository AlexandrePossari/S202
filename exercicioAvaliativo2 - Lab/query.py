from database import Database

db = Database(
    'neo4j+s://54f4fa39.databases.neo4j.io',
    'neo4j',
    'mXNfxrDccsf4jixvUl2c7x5k51B711__j2ZXQkNB_0Q'
)
db.reset_db()

query = 'MATCH (t:Teacher {name: $name}) RETURN t.ano_nasc AS ano_nasc, t.cpf AS cpf;'
parameters = {"name": "Renzo"}

results = db.execute_query(query, parameters)

ano_nasc = results[0]['ano_nasc']
cpf = results[0]['cpf']

print('Questão 01\n')
print("A)\n")
print(f'ano_nasc: {ano_nasc}\n')
print(f'cpf: {cpf}\n')

query = 'MATCH (t:Teacher) WHERE t.name STARTS WITH "M" RETURN t.name AS name, t.cpf AS cpf;'

results = [
    {
        'name': row['name'],
        'cpf': row['cpf']
    }
    for row in db.execute_query(query)
]

print('B)\n')

for row in results:
    for key, value in row.items():
        print(f'{key}: {value}\n')

query = 'MATCH (c:City) RETURN c.name AS name;'

results = [r['name'] for r in db.execute_query(query)]

print('C)\n')
for cityName in results:
    print(f'{cityName}\n')

query = 'MATCH (s:School) WHERE s.number >= 150 AND s.number <= 550 RETURN s.name AS name, s.address AS address;'

results = [
    {
        'name': row['name'],
        'address': row['address']
    }
    for row in db.execute_query(query)
]

print('D)\n')
for row in results:
    for key, value in row.items():
        print(f'{key}: {value}\n')

query = 'MATCH (t:Teacher) RETURN min(t.ano_nasc) AS mais_velho_ano_nasc, max(t.ano_nasc) AS mais_novo_ano_nasc;'

mais_velho_ano_nasc = db.execute_query(query)[0]['mais_velho_ano_nasc']
mais_novo_ano_nasc = db.execute_query(query)[0]['mais_novo_ano_nasc']

print('Questão 02\n')
print('A)\n')
print(f'Professor mais jovem: {mais_novo_ano_nasc}\n')
print(f'Professor mais velho: {mais_velho_ano_nasc}\n')

query = 'MATCH (c:City) RETURN avg(c.population) as media_pop;'
result = db.execute_query(query)[0]['media_pop']

print('B)\n')
print(f'Média: {result}\n')

query = 'MATCH (c:City {cep: "37540-000"}) RETURN replace(c.name, "a", "A") AS nome_substituido;'
result = db.execute_query(query)[0]['nome_substituido']

print('C)\n')
print(f'{result}\n')

query = 'MATCH (n:Teacher) RETURN substring(n.name, 3, 1) AS a_partir_letra_3;'
results = [result['a_partir_letra_3'] for result in db.execute_query(query)]

print('D)\n')
for result in results:
    print(f'{result}\n')