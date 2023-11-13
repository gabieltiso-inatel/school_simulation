from database import Database
from teacher_crud import TeacherCrud

from cli import TeacherCLI

db = Database("bolt://3.86.240.30:7687", "neo4j", "slaps-connection-guards")
db.drop_all()

t_crud = TeacherCrud(db)

t_crud.create(name="Chris Lima", ano_nasc=1956, cpf="189.052.396-66")
print(t_crud.read("Chris Lima"))

t_crud.update("Chris Lima", "162.052.777-77")

teacher_cli = TeacherCLI(t_crud)
teacher_cli.run()
