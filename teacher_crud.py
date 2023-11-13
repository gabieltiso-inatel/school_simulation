from database import Database

class TeacherCrud():
    def __init__(self, database: Database):
        self.db = database

    def create(self, name, ano_nasc, cpf):
        query = "CREATE (:Teacher{name: $name, ano_nasc: $ano_nasc, cpf: $cpf})"
        parameters = {"name": name, "ano_nasc": ano_nasc, "cpf": cpf}
        self.db.execute_query(query, parameters)

    def delete(self, name):
        query = "MATCH (t:Teacher{name: $name}) DETACH DELETE t"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)

    def read(self, name):
        query = "MATCH (t:Teacher{name: $name}) RETURN t.name as name, t.cpf as cpf, t.ano_nasc as ano_nasc"
        parameters = {"name": name}
        results = self.db.execute_query(query, parameters)

        return [(result["name"], result["ano_nasc"], result["cpf"]) for result in results]

    def update(self, name, newCpf):
        query = "MATCH (t:Teacher{name: $name}) SET t.cpf = $newCpf"
        parameters = {"name": name, "newCpf": newCpf}
        self.db.execute_query(query, parameters)
