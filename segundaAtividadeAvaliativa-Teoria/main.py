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


def get_vendedores(tx):
    query = """
        MATCH (n:Pessoa:Vendedor) RETURN n;
    """
    try:
        result = tx.run(query)
        print(result)
        return result
 
    except ServiceUnavailable as exception:
 
        print("{query} raised an error: \n {exception}".format(query=query, exception=exception))
 
        raise

def get_filho_de_quem(tx, filho):
    query = """
        MATCH ({nome:"$filho"})-[:FILHO_DE]->(p) RETURN p;
    """
    try:
        result = tx.run(query.replace("$filho", filho))
        print(result)
        return result
 
    except ServiceUnavailable as exception:
 
        print("{query} raised an error: \n {exception}".format(query=query, exception=exception))
 
        raise

def get_irmao_de(tx):
    query = """
        MATCH p=()-[:IRMAO_DE]->() RETURN p;
    """
    try:
        result = tx.run(query)
        print(result)
        return result
 
    except ServiceUnavailable as exception:
 
        print("{query} raised an error: \n {exception}".format(query=query, exception=exception))
 
        raise
 
uri = "neo4j+s://94610b1a.databases.neo4j.io"
user = "neo4j"
password = "DoJrS1qzpyDhAlHDnZGWcRltB8YFCvIyUKDizDk1UlA"
 
print("test1") 
driver = GraphDatabase.driver(uri, auth=(user, password))
 
print("test2")  
with driver.session() as session:
    session.execute_write(get_vendedores)
 
n = 4 
while(n != 0):    
    print("1 - Quem da família é Vendedor?")
    print("2 - X pessoa é filho de quem?")
    print("3 - Quem é irmão de quem?")
    print("0 - Sair do programa")
    n = input("Opção do menu?")

    if n == 1:
        with driver.session() as session:
            session.execute_write(get_vendedores)    
    elif n == 2:
        filho = input("Nome do filho?")
        with driver.session() as session:
            session.execute_write(get_filho_de_quem, filho)  
    elif n == 3:
        with driver.session() as session:
            session.execute_write(get_irmao_de)  


driver.close()