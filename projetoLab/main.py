from projetoLab.user_cli import UserCLI
from projetoLab.User_DAO import UserDAO

if __name__ == '__main__':
    motoristaDAO = UserDAO('exav1', 'Motoristas')
    cli = UserCLI(motoristaDAO)
    cli.run()