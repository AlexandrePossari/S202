from user_cli import UserCLI
from User_DAO import UserDAO

if __name__ == '__main__':
    userDao = UserDAO('Projeto', 'Users')
    cli = UserCLI(userDao)
    cli.run()