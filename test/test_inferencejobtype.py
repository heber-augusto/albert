#import sys
#sys.path.append('/home/ubuntu/projetos/albert')
import os
from albert.jobtypes.jobtype import InferenceJobType
import shutil
import threading
import time
import pytest
from test.docker_utils import *

def test_inference_create():
    # Teste de criação de InferenceJobType
    inference_job = InferenceJobType('inference_test')
    destination_folder = 'test_destination'
    inference_job.create(destination_folder)
    assert inference_job.name == 'inference_test'
    assert inference_job.uuid is not None
    shutil.rmtree(destination_folder, ignore_errors=True)

def test_inference_run():
    # Teste de execução de InferenceJobType
    inference_job = InferenceJobType('inference_test')
    try:
        inference_job.run()
        assert True  # Método run está implementado
    except NotImplementedError:
        assert False, "Método run não deveria gerar exceção"

def test_inference_check():
    # Teste de verificação de testes de InferenceJobType
    inference_job = InferenceJobType('inference_test')
    destination_folder = 'test_destination'
    inference_job.create(destination_folder)
    os.chdir(os.path.join(destination_folder, 'inference_test'))
    try:
        retcode, stdout = inference_job.check()

        # Agora, 'output' contém a saída do comando como uma string, e 'return_code' contém o código de retorno
        print("Saída do comando:\n", stdout)
        print("Código de retorno:", retcode)

        assert (retcode == 1)  # Método check está implementado
    except:
        assert False, "Método check não deveria gerar exceção"
    os.chdir('../../')
    shutil.rmtree(destination_folder, ignore_errors=True)
    assert True

# Variável compartilhada para armazenar informações da thread
#container_info = {}

# Função para iniciar o contêiner Docker em uma thread separada
def threaded_run_command(**kwargs):
    container_info = kwargs['container_info']
    # Teste de verificação de testes de InferenceJobType
    inference_job = InferenceJobType('inference_test')
    destination_folder = 'test_destination'
    inference_job.create(destination_folder)
    try:
        os.chdir(os.path.join(destination_folder, 'inference_test'))
        retcode, stdout = inference_job.run()

        # Agora, 'output' contém a saída do comando como uma string, e 'return_code' contém o código de retorno
        container_info.stdout = stdout
        container_info.retcode = retcode
        assert (retcode == 0)  # Execução do container não gera erro
    except:
        assert False, "Método run não deveria gerar exceção"
    os.chdir('../../')        
    shutil.rmtree(destination_folder, ignore_errors=True)
    assert True


def test_inference_run():
    #testa se aplicação está rodando no começo
    assert not is_application_running()
    create_thread_to_execute(
        threaded_run_function=threaded_run_command, 
        job_type = 'inference', 
        job_name = 'inference_test'       

    )
    assert not is_application_running()


# # Função para iniciar o contêiner Docker em uma thread separada
# def threaded_deploy_command(**kwargs):
#     container_info = kwargs['container_info']
#     # Teste de verificação de testes de InferenceJobType
#     inference_job = InferenceJobType('inference_test')
#     destination_folder = 'test_destination'
#     inference_job.create(destination_folder)
#     try:
#         os.chdir(os.path.join(destination_folder, 'inference_test'))
#         retcode, stdout = inference_job.deploy()

#         # Agora, 'output' contém a saída do comando como uma string, e 'return_code' contém o código de retorno
#         container_info.stdout = stdout
#         container_info.retcode = retcode
#         assert (retcode == 0)  # Execução do container não gera erro
#     except:
#         assert False, "Método deploy não deveria gerar exceção"
#     os.chdir('../../')        
#     shutil.rmtree(destination_folder, ignore_errors=True)
#     assert True


# def test_inference_deploy():
#     #testa se aplicação está rodando no começo
#     assert not is_application_running()
#     create_thread_to_execute(
#         threaded_run_function=threaded_deploy_command, 
#         job_type = 'inference', 
#         job_name = 'inference_test'       

#     )
#     assert not is_application_running()


