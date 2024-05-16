from teacher_crud import TeacherCRUD


class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            print(f'Commands: {["create", "read", "update", "delete", "quit"]}')
            command = input("Enter a command: ")
            if command == "quit":
                print("Goodbye!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Invalid command. Try again.")


class TeacherCLI(SimpleCLI):
    def __init__(self, teacherCRUD: TeacherCRUD):
        super().__init__()
        self._teacherCRUD = teacherCRUD
        self.add_command("create", self.criar_professor)
        self.add_command("read", self.ler_professor)
        self.add_command("update", self.atualizar_professor)
        self.add_command("delete", self.deletar_professor)

    def criar_professor(self):
        name = input('Nome: ')
        ano_nasc = input('Ano de nascimento: ')
        cpf = input('Cpf: ')

        self._teacherCRUD.create(name, ano_nasc, cpf)

        print('Professor criado!')

    def ler_professor(self):
        name = input('Nome: ')

        teacher = self._teacherCRUD.read(name)

        if teacher:
            print('Professor encontrado:')
            for key, value in teacher.items():
                print(f'{key}: {value}\n')
        else:
            print('Professor não encontrado!')

    def atualizar_professor(self):
        name = input('Nome: ')
        newCpf = input('Novo CPF: ')

        teacher = self._teacherCRUD.update(name, newCpf)

        if teacher:
            print('Professor atualizado:')
            for key, value in teacher.items():
                print(f'{key}: {value}\n')
        else:
            print('Professor não encontrado!')

    def deletar_professor(self):
        nome = input("Nome: ")
        self._teacherCRUD.delete(nome)

        print('Professor deletado')

    def run(self):
        super().run()