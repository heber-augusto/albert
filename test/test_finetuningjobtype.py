#import sys
#sys.path.append('/home/ubuntu/projetos/albert')
import os
from albert.jobtypes.jobtype import FineTuningJobType
import shutil
import threading
import time
import pytest
from test.docker_utils import *

def test_finetuning_create():
    # Teste de criação de FineTuningJobType
    finetuning_job = FineTuningJobType('finetuning_test')
    destination_folder = 'test_destination'
    finetuning_job.create(destination_folder)
    assert finetuning_job.name == 'finetuning_test'
    assert finetuning_job.uuid is not None
    shutil.rmtree(destination_folder, ignore_errors=True)

def test_finetuning_check():
    # Teste de verificação de testes de FineTuningJobType
    finetuning_job = FineTuningJobType('finetuning_test')
    destination_folder = 'test_destination'
    finetuning_job.create(destination_folder)
    os.chdir(os.path.join(destination_folder, 'finetuning_test'))
    try:
        retcode, stdout = finetuning_job.check()

        # Agora, 'output' contém a saída do comando como uma string, e 'return_code' contém o código de retorno
        print("Saída do comando:\n", stdout)
        print("Código de retorno:", retcode)

        assert (retcode == 1)  # Método check está implementado
    except:
        assert False, "Método check não deveria gerar exceção"
    os.chdir('../../')
    shutil.rmtree(destination_folder, ignore_errors=True)
    assert True

# Função para iniciar o contêiner Docker em uma thread separada
def threaded_run_command(**kwargs):
    container_info = kwargs['container_info']
    # Teste de verificação de testes de FineTuningJobType
    finetuning_job = FineTuningJobType('finetuning_test')
    destination_folder = 'test_destination'
    finetuning_job.create(destination_folder)

    template_code_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'template_files',
        'finetuning_code.py'
    )


    try:
        os.chdir(os.path.join(destination_folder, 'finetuning_test'))

        shutil.copyfile(
            template_code_path, 
            './source/code.py')

        retcode, stdout = finetuning_job.run()

        # Agora, 'output' contém a saída do comando como uma string, e 'return_code' contém o código de retorno
        container_info.stdout = stdout
        container_info.retcode = retcode
        assert (retcode == 1)  # Execução do container gera erro pois funções não estão implementadas
        assert (stdout.find('raise NotImplementedError()') > 0)
    except:
        assert False, "Método run não deveria gerar exceção"
    os.chdir('../../')        
    shutil.rmtree(destination_folder, ignore_errors=True)
    assert True


def test_finetuning_run():
    #testa se aplicação está rodando no começo
    job_type = 'finetuning' 
    job_name = 'finetuning_test'    
    assert not check_container_running(job_type,job_name)
    create_thread_to_execute(
        threaded_run_function=threaded_run_command, 
        job_type = job_type, 
        job_name = job_name,
        is_application_running=dummy_check_container_running       

    )
    assert not check_container_running(job_type,job_name)


# # Função para iniciar o contêiner Docker em uma thread separada
# def threaded_deploy_command(**kwargs):
#     container_info = kwargs['container_info']
#     # Teste de verificação de testes de FineTuningJobType
#     finetuning_job = FineTuningJobType('finetuning_test')
#     destination_folder = 'test_destination'
#     finetuning_job.create(destination_folder)
#     try:
#         os.chdir(os.path.join(destination_folder, 'finetuning_test'))
#         retcode, stdout = finetuning_job.deploy()

#         # Agora, 'output' contém a saída do comando como uma string, e 'return_code' contém o código de retorno
#         container_info.stdout = stdout
#         container_info.retcode = retcode
#         assert (retcode == 0)  # Execução do container não gera erro
#     except:
#         assert False, "Método deploy não deveria gerar exceção"
#     os.chdir('../../')        
#     shutil.rmtree(destination_folder, ignore_errors=True)
#     assert True


# def test_finetuning_deploy():
#     #testa se aplicação está rodando no começo
#     assert not is_application_running()
#     create_thread_to_execute(
#         threaded_run_function=threaded_deploy_command, 
#         job_type = 'finetuning', 
#         job_name = 'finetuning_test'       

#     )
#     assert not is_application_running()


