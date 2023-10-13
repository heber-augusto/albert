import os
import json
import argparse

from albert.jobtypes.jobtype import *

job_type_name_2_class = {
    'inference':InferenceJobType,
    'finetuning':FineTuningJobType,    
}

 
def load_config_json_to_dict(json_path):
    # Opening JSON file
    with open(json_path) as json_file:
        data = json.load(json_file)
    return data

class JobCommand:
    """
    Classe base para comandos de gerenciamento de job types.

    Métodos:
        execute(): Executa o comando. Deve ser implementado nas classes especializadas.
        add_parser(subparsers): Adiciona um subparser para o comando.
    """
    def __init__(self, args):
        self.args = args

    @staticmethod
    def get_job_class(jobtype):
        """
        Obtém a classe de job type associada com o nome especificado (inference ou finetune).

        Args:
            jobtype (str): Nome do tipo de job (inference ou finetune).

        Returns:
            class: A classe de job type associada ao nome especificado.
        """
        job_type_class = job_type_name_2_class[jobtype]
    
        return job_type_class

    def execute(self):
        raise NotImplementedError("Método execute não implementado")

    def add_parser(self, subparsers):
        raise NotImplementedError("Método add_parser não implementado")

class CreateCommand(JobCommand):
    """
    Comando para criar um novo job type.

    Args:
        args: Argumentos da linha de comando.
    """
    def __init__(self, args):
        super().__init__(args)

    def execute(self):
        jobtype = self.args.jobtype
        folder_name = self.args.folder_name
        destination_folder = self.args.destination_folder

        job_type_class = self.get_job_class(jobtype)
        job_type_instance = job_type_class(folder_name)

        destination_folder = destination_folder or os.getcwd()
        job_type_instance.create(destination_folder)

    def add_parser(self, subparsers):
        parser = subparsers.add_parser("create", help="Cria um novo job type.")
        parser.add_argument("jobtype", choices=["inference", "finetune"], help="Tipo de job (inference ou finetune).")
        parser.add_argument("folder_name", help="Nome de identificação da pasta.")
        parser.add_argument("destination_folder", nargs="?", help="Pasta de destino opcional.")

class CheckCommand(JobCommand):
    """
    Comando para verificar os testes de um job type.

    Args:
        args: Argumentos da linha de comando.
    """
    def __init__(self, args):
        super().__init__(args)

    def execute(self):
        config = load_config_json_to_dict('config.json')
        job_type = config['type']

        job_type_class = self.get_job_class(job_type)
        job_type_instance = job_type_class(config['name'])
        return job_type_instance.check()

    def add_parser(self, subparsers):
        subparsers.add_parser("check", help="Verifica os testes do job type atual.")

class RunCommand(JobCommand):
    """
    Comando para executar um job type.

    Args:
        args: Argumentos da linha de comando.
    """
    def __init__(self, args):
        super().__init__(args)

    def execute(self):
        config = load_config_json_to_dict('config.json')
        job_type = config['type']

        job_type_class = self.get_job_class(job_type)
        job_type_instance = job_type_class(config['name'])
        return job_type_instance.run()

    def add_parser(self, subparsers):
        subparsers.add_parser("run", help="Executa o job type atual.")

class DeployCommand(JobCommand):
    """
    Comando para realizar o deploy de um job type.

    Args:
        args: Argumentos da linha de comando.
    """
    def __init__(self, args):
        super().__init__(args)

    def execute(self):
        config = load_config_json_to_dict('config.json')
        job_type = config['type']

        job_type_class = self.get_job_class(job_type)
        job_type_instance = job_type_class(config['name'])
        return job_type_instance.deploy()

    def add_parser(self, subparsers):
        subparsers.add_parser("deploy", help="Realiza o deploy do job type atual.")


def load_and_config_parser():
    parser = argparse.ArgumentParser(description="Comandos para gerenciamento de job types.")
    subparsers = parser.add_subparsers(dest="command", help="Comandos disponíveis.")

    commands = [
        CreateCommand,
        CheckCommand,
        RunCommand,
        DeployCommand
    ]

    for command_class in commands:
        command = command_class(None)
        command.add_parser(subparsers)
    return parser 