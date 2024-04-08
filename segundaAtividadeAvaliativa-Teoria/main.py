from neo4j import GraphDatabase
from neo4j.exceptions import ServiceUnavailable
 
def create_and_return_example(tx, nome, tipo, profissao):
        query = """
            CREATE(n:$tipo:$profissao)
        """
        print(query)
        result = tx.run(
            query,
            tipo = tipo,
            profissao = profissao
        )
 
        try:
            return [{"tipo": row["n"]["tipo"]} for row in result]
 
        # Capture any errors along with the query and data for traceability
 
        except ServiceUnavailable as exception:
 
            print("{query} raised an error: \n {exception}".format(query=query, exception=exception))
 
            raise
 
def get_amount_data(tx):
    query = """
        MATCH(n) RETURN COUNT(n) AS amount;
    """
    try:
        result = tx.run(query)
        return [{
            'amount':row['amount']
        } for row in result]
 
    except ServiceUnavailable as exception:
 
        print("{query} raised an error: \n {exception}".format(query=query, exception=exception))
 
        raise
 
uri = ""
user = ""
password = ""
 
driver = GraphDatabase.driver(uri, auth=(user, password))
 
 
with driver.session() as session:
    session.execute_write(create_and_return_example, "Paulo", "Pessoa", "Agricultor")
    session.execute_write(create_and_return_example, "Isaura", "Pessoa", "Agricultora")
    session.execute_write(create_and_return_example, "José", "Pessoa", "Caminhoneiro")
    session.execute_write(create_and_return_example, "Maiesse", "Pessoa", "Diarista")
    session.execute_write(create_and_return_example, "Valmir", "Pessoa", "Vendedor")
    session.execute_write(create_and_return_example, "Rossemi", "Pessoa", "Empilhadeirista")
    session.execute_write(create_and_return_example, "Alexandre", "Pessoa", "Estudante")
    session.execute_write(create_and_return_example, "Felipe", "Pessoa", "Engenheiro")
    session.execute_write(create_and_return_example, "Fernando", "Pessoa", "Vendedor")
    session.execute_write(create_and_return_example, "Zézinho", "Pessoa", "Caminhoneiro")
 
with driver.session() as session:
    result = session.execute_read(get_amount_data)
    print(result[0]['amount'])
driver.close()