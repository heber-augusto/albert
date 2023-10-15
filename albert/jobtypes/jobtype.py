import os
import shutil
import json
import uuid
import subprocess

class JobType:
    """
    Classe base para tipos de job de machine learning.

    Args:
        name (str): Nome do tipo de job.

    Attributes:
        name (str): Nome do job.
        type (str): Tipo de job.
        uuid (str): UUID de identificação.
        config (dict): Dicionário de configuração.

    Methods:
        create(destination_folder: str): Cria a estrutura de pastas do job type.
        run(): Executa o job.
        deploy(): Realiza o deploy do job.
        check(): Executa testes para o job type.
    """
    def __init__(self, name: str, type: str):
        self.name = name
        self.uuid = str(uuid.uuid4())
        self.type = type
        self.config = {
            'uuid': self.uuid,
            'type': self.type,
            'name': self.name
        }

    def create(self, destination_folder: str):
        """
        Cria a estrutura de pastas do job type.

        Args:
            destination_folder (str): Caminho para a pasta de destino.
        """
        # Obtém o diretório do arquivo jobtype.py
        jobtype_directory = os.path.dirname(os.path.abspath(__file__))

        # Concatena o caminho do template com o diretório do arquivo jobtype.py
        template_path = os.path.join(jobtype_directory, self.template_path)

        jobtype_folder = os.path.join(destination_folder, self.name)
        os.makedirs(jobtype_folder, exist_ok=True)
        shutil.copytree(
            template_path, 
            jobtype_folder, 
            dirs_exist_ok = True)

        config_path = os.path.join(jobtype_folder, 'config.json')
        with open(config_path, 'w') as config_file:
            json.dump(self.config, config_file)

    def run(self):
        """
        Executa o job. Deve ser implementado nas classes especializadas.
        Args:
            destination_folder (str): Caminho para a pasta onde o código do job está presente.        
        """
        raise NotImplementedError("Método run não implementado")

    def deploy(self):
        """
        Realiza o deploy do job. Deve ser implementado nas classes especializadas.
        Args:
            destination_folder (str): Caminho para a pasta onde o código do job está presente.                
        """
        raise NotImplementedError("Método deploy não implementado")

    def check(self):
        """
        Executa testes do job type. Utiliza pytest para verificar os testes na raiz da pasta do job type.
        """
        # Executa o comando e redireciona a saída para um objeto PIPE
        pytest_process = subprocess.Popen(
            [r'pytest', "-rf", "--tb=line"],
            stdout=subprocess.PIPE,  # Redireciona a saída padrão para um PIPE
            text=True
        )

        # Lê a saída do comando
        output, _ = pytest_process.communicate()

        # Obtém o código de retorno do processo
        return_code = pytest_process.returncode

        if return_code is None or return_code == 0:
            print(f'Testes para {self.name} passaram com sucesso.')
        else:
            print(f'Testes para {self.name} falharam.')
        return return_code, output

class InferenceJobType(JobType):
    """
    Classe especializada para job type de inferência.

    Args:
        name (str): Nome do job type.
        inference_model (str): Nome do modelo de inferência.

    Methods:
        run(): Executa a inferência do modelo.
        deploy(): Realiza o deploy do modelo de inferência.
    """
    template_path = 'templates/inference'  # Caminho fixo para arquivos de template

    def __init__(self, name: str):
        super().__init__(
            name=name,
            type = 'inference')

    def run(self):
        """
        Executa a inferência do modelo de inferência especificado.
        Args:
            destination_folder (str): Caminho para a pasta onde o código do job está presente.        
        """
        run_folder = os.path.join('.', 'source')

        # Primeiro, construa a imagem Docker
        build_command = ["docker", "build", "-t", f"albert-inference-job-{self.name}", "."]
        subprocess.run(build_command, cwd=run_folder)

        # Em seguida, execute o contêiner Docker
        run_command = ["docker", "run", "-p","5000:5000", "-t", f"albert-inference-job-{self.name}"]
        
        run_process = subprocess.Popen(
             run_command,
             stdout=subprocess.PIPE,
             stderr=subprocess.STDOUT,
             text=True,
             cwd=run_folder
        )
        # Aguarda a conclusão do processo ou sinal SIGINT (Ctrl+C)
        output = ""
        try:
            # Leitura e exibição contínua da saída do contêiner
            for line in run_process.stdout:
                print(line, end='')
                output += line

            run_process.wait()
        except KeyboardInterrupt:
            # Tratamento de Ctrl+C
            print("Recebido Ctrl+C. Encerrando o contêiner.")

        # Obtém o código de retorno do processo
        return_code = run_process.returncode

        if return_code is None or return_code == 0:
            print(f'Build para {self.name} concluído com sucesso.')
        else:
            print(f'Build para {self.name} falharam.')
        return return_code, output



    def deploy(self):
        """
        Realiza o deploy do modelo de inferência especificado.
        Args:
            destination_folder (str): Caminho para a pasta onde o código do job está presente.        
        """
        """
        Executa a inferência do modelo de inferência especificado.

        """
        run_folder = os.path.join('.', 'deploy')

        # Primeiro, altera permissão do shell de deploy
        chmod_command = ["chmod", "+x", "deploy.sh"]
        subprocess.run(chmod_command, cwd=run_folder)

        # Em seguida, execute o contêiner Docker
        run_command = ["sh", "./deploy.sh"]
        
        run_process = subprocess.Popen(
             run_command,
             stdout=subprocess.PIPE,
             stderr=subprocess.STDOUT,
             text=True,
             cwd=run_folder
        )
        # Aguarda a conclusão do processo ou sinal SIGINT (Ctrl+C)
        output = ""
        try:
            # Leitura e exibição contínua da saída do Deploy
            for line in run_process.stdout:
                print(line, end='')
                output += line

            run_process.wait()
        except KeyboardInterrupt:
            # Tratamento de Ctrl+C
            print("Recebido Ctrl+C. Encerrando o Deploy.")

        # Obtém o código de retorno do processo
        return_code = run_process.returncode

        if return_code is None or return_code == 0:
            print(f'Deploy para {self.name} concluído com sucesso.')
        else:
            print(f'Deploy para {self.name} falharam.')
        return return_code, output

class FineTuningJobType(JobType):
    """
    Classe especializada para job type de fine-tuning.

    Args:
        name (str): Nome do job type.
        model_to_finetune (str): Nome do modelo a ser fine-tuned.

    Methods:
        run(): Executa o fine-tuning do modelo.
        deploy(): Realiza o deploy do modelo fine-tuned.
    """
    template_path = 'templates/finetuning'  # Caminho fixo para arquivos de template

    def __init__(self, name: str):
        super().__init__(
            name = name,
            type = 'finetuning')

    def run(self):
        """
        Executa o fine-tuning do modelo especificado.
        Args:
            destination_folder (str): Caminho para a pasta onde o código do job está presente.        
        """
        print(f'Executando fine-tuning do modelo: {self.config["model_to_finetune"]}')

    def deploy(self):
        """
        Realiza o deploy do modelo fine-tuned especificado.
        Args:
            destination_folder (str): Caminho para a pasta onde o código do job está presente.        
        """
        print(f'Realizando deploy do modelo: {self.config["model_to_finetune"]}')

# Exemplos de uso:
# job_type = JobType('inference')
# job_type.create('destination_folder')
# job_type.run()
# job_type.deploy()
# job_type.check()
# inference_job = InferenceJobType('inference', 'model_name')
# inference_job.create('destination_folder')
# inference_job.run()
# inference_job.deploy()
# inference_job.check()
# finetuning_job = FineTuningJobType('fine-tuning', 'base_model')
# finetuning_job.create('destination_folder')
# finetuning_job.run()
# finetuning_job.deploy()
# finetuning_job.check()
