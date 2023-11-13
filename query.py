from database import Database

db = Database("bolt://3.86.240.30:7687", "neo4j", "slaps-connection-guards")

def print_results(results):
    for result in results:
        print(result)

### Questão 1 ###

query_q1_a = "MATCH (t:Teacher{name: 'Renzo'}) RETURN t.ano_nasc, t.cpf;"
results = db.execute_query(query_q1_a)
print(f"Q1, letra a): ")
print_results(results)
print()

query_q1_b = """
MATCH (t:Teacher)
WHERE t.name STARTS WITH 'M'
RETURN t.name, t.cpf;
"""
results = db.execute_query(query_q1_b)
print(f"Q1, letra b): ")
print_results(results)
print()

query_q1_c = "MATCH (c:City) RETURN c.name;"
results = db.execute_query(query_q1_c)
print(f"Q1, letra c): ")
print_results(results)
print()

query_q1_d = """
MATCH (s:School)
WHERE s.number >= 150 OR s.number <= 550
RETURN s.name, s.address, s.number;
"""
results = db.execute_query(query_q1_d)
print(f"Q1, letra d): ")
print_results(results)
print()

### Questão 2 ###

query_q2_a = "MATCH (t:Teacher) RETURN MAX(t.ano_nasc), MIN(t.ano_nasc);"
results = db.execute_query(query_q2_a)
print(f"Q2, letra a): ")
print_results(results)
print()

query_q2_b = "MATCH (c:City) RETURN AVG(c.population);"
results = db.execute_query(query_q2_b)
print(f"Q2, letra b): ")
print_results(results)
print()

query_q2_c = "MATCH (c:City{cep: '37540-000'}) RETURN REPLACE(c.name, 'a', 'A');"
results = db.execute_query(query_q2_c)
print(f"Q2, letra c): ")
print_results(results)
print()

# query_q2_d = ""
# print(query_q2_d)
