from teacher_cli import TeacherCLI
from teacher_crud import TeacherCRUD

if __name__ == '__main__':
    teacherCRUD = TeacherCRUD(
        'neo4j+s://54f4fa39.databases.neo4j.io',
        'neo4j',
        'mXNfxrDccsf4jixvUl2c7x5k51B711__j2ZXQkNB_0Q'
    )
    cli = TeacherCLI(teacherCRUD)
    cli.run()

    teacherCRUD.close()