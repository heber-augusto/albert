#import sys
#sys.path.append('/home/ubuntu/projetos/albert')
import os
from albert.jobtypes.jobtype import InferenceJobType
import shutil
import threading
import requests
import time
import pytest
import subprocess

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

def test_inference_deploy():
    # Teste de deploy de InferenceJobType
    inference_job = InferenceJobType('inference_test')
    try:
        destination_folder = 'test_destination'
        inference_job.deploy(destination_folder)
        assert True  # Método deploy está implementado
    except NotImplementedError:
        assert False, "Método deploy não deveria gerar exceção"

def test_inference_check():
    # Teste de verificação de testes de InferenceJobType
    inference_job = InferenceJobType('inference_test')
    destination_folder = 'test_destination'
    inference_job.create(destination_folder)
    try:
        retcode, stdout = inference_job.check(destination_folder)

        # Agora, 'output' contém a saída do comando como uma string, e 'return_code' contém o código de retorno
        print("Saída do comando:\n", stdout)
        print("Código de retorno:", retcode)

        assert (retcode == 1)  # Método check está implementado
    except:
        assert False, "Método check não deveria gerar exceção"
    shutil.rmtree(destination_folder, ignore_errors=True)
    assert True


# Função para verificar se a aplicação Flask está rodando
def is_application_running():
    url = "http://localhost:5000"  # URL da aplicação Flask no contêiner
    try:
        response = requests.get(url)
        return response.status_code == 200
    except requests.RequestException:
        return False

# Função para interromper o contêiner Docker
def stop_container():
    os.system('docker rm $(docker stop $(docker ps -a -q --filter ancestor=albert-inference-job-inference_test --format="{{.ID}}"))')

# Variável compartilhada para armazenar informações da thread
container_info = {}

# Função para iniciar o contêiner Docker em uma thread separada
def threaded_run_command():
    # Teste de verificação de testes de InferenceJobType
    inference_job = InferenceJobType('inference_test')
    destination_folder = 'test_destination'
    inference_job.create(destination_folder)
    try:
        retcode, stdout = inference_job.run(destination_folder)

        # Agora, 'output' contém a saída do comando como uma string, e 'return_code' contém o código de retorno
        container_info['stdout'] = stdout
        container_info['retcode'] = retcode
        assert (retcode == 0)  # Execução do container não gera erro
    except:
        assert False, "Método run não deveria gerar exceção"
    shutil.rmtree(destination_folder, ignore_errors=True)
    assert True


def test_inference_run():
    #testa se aplicação está rodando no começo
    assert not is_application_running()
    
    # Iniciar o contêiner Docker em uma thread separada
    container_thread = threading.Thread(target=threaded_run_command)
    container_thread.start()

    # Aguardar até que a aplicação no contêiner esteja em execução
    for _ in range(30):  # Aguarda por até 300 segundos
        if is_application_running():
            break
        time.sleep(10)
    else:
        pytest.fail("A aplicação no contêiner não iniciou a tempo.")

    # Execute os testes específicos no contêiner (opcional)

    # Interrompa o contêiner Docker
    stop_container()

    # Verifique se o contêiner foi interrompido
    container_thread.join()  # Aguarde a thread do contêiner encerrar

    print("Saída do comando:\n", container_info['stdout'])
    print("Código de retorno:", container_info['retcode'])

    assert container_info['retcode'] == 0
    assert not is_application_running()


#test_inference_run()