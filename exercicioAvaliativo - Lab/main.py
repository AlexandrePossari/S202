from motorista_cli import MotoristaCLI
from motorista_DAO import MotoristaDAO

if __name__ == '__main__':
    motoristaDAO = MotoristaDAO('exav1', 'Motoristas')
    cli = MotoristaCLI(motoristaDAO)
    cli.run()