import os
import shutil
import json
import pytest
import uuid

class JobType:
    """
    Classe base para tipos de job de machine learning.

    Args:
        name (str): Nome do tipo de job.

    Attributes:
        name (str): Nome do tipo de job.
        uuid (str): UUID de identificação.
        config (dict): Dicionário de configuração.

    Methods:
        create(destination_folder: str): Cria a estrutura de pastas do job type.
        run(): Executa o job.
        deploy(): Realiza o deploy do job.
        check(): Executa testes para o job type.
    """
    def __init__(self, name: str):
        self.name = name
        self.uuid = str(uuid.uuid4())
        self.config = {
            'uuid': self.uuid
        }

    def create(self, destination_folder: str):
        """
        Cria a estrutura de pastas do job type.

        Args:
            destination_folder (str): Caminho para a pasta de destino.
        """
        jobtype_folder = os.path.join(destination_folder, self.name)
        os.makedirs(jobtype_folder, exist_ok=True)

        for file in os.listdir(self.template_path):
            src = os.path.join(self.template_path, file)
            dest = os.path.join(jobtype_folder, file)
            shutil.copy(src, dest)

        config_path = os.path.join(jobtype_folder, 'config.json')
        with open(config_path, 'w') as config_file:
            json.dump(self.config, config_file)

    def run(self):
        """
        Executa o job. Deve ser implementado nas classes especializadas.
        """
        raise NotImplementedError("Método run não implementado")

    def deploy(self):
        """
        Realiza o deploy do job. Deve ser implementado nas classes especializadas.
        """
        raise NotImplementedError("Método deploy não implementado")

    def check(self):
        """
        Executa testes do job type. Utiliza pytest para verificar os testes na raiz da pasta do job type.
        """
        jobtype_folder = os.path.join(self.name)
        result = pytest.main([jobtype_folder])
        if result is None or result == 0:
            print(f'Testes para {self.name} passaram com sucesso.')
        else:
            print(f'Testes para {self.name} falharam.')

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

    def __init__(self, name: str, inference_model: str):
        super().__init__(name)
        self.config['inference_model'] = inference_model

    def run(self):
        """
        Executa a inferência do modelo de inferência especificado.
        """
        print(f'Executando inferência do modelo: {self.config["inference_model"]}')

    def deploy(self):
        """
        Realiza o deploy do modelo de inferência especificado.
        """
        print(f'Realizando deploy do modelo: {self.config["inference_model"]}')

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

    def __init__(self, name: str, model_to_finetune: str):
        super().__init__(name)
        self.config['model_to_finetune'] = model_to_finetune

    def run(self):
        """
        Executa o fine-tuning do modelo especificado.
        """
        print(f'Executando fine-tuning do modelo: {self.config["model_to_finetune"]}')

    def deploy(self):
        """
        Realiza o deploy do modelo fine-tuned especificado.
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
