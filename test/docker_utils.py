import pytest
import requests
import os
import threading
import time

# Função para interromper o contêiner Docker
def stop_container(job_type, job_name):
    os.system(f'docker rm $(docker stop $(docker ps -a -q --filter ancestor=albert-{job_type}-job-{job_name}' + ' --format="{{.ID}}"))')


# Função para verificar se a aplicação Flask está rodando
def is_application_running():
    url = "http://localhost:5000"  # URL da aplicação Flask no contêiner
    try:
        response = requests.get(url)
        return response.status_code == 200
    except requests.RequestException:
        return False


class ContainerInfo:
    """
    Classe para guardar informações de retorno do container.
    """
    def __init__(self):
        self.stdout = ''
        self.retcode = -1


def create_thread_to_execute(threaded_run_function, job_type, job_name):
    container_info = ContainerInfo()
    # Iniciar o contêiner Docker em uma thread separada
    container_thread = threading.Thread(
        target=threaded_run_function, 
        kwargs={'container_info':container_info,})
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
    stop_container(job_type, job_name)

    # Verifique se o contêiner foi interrompido
    container_thread.join()  # Aguarde a thread do contêiner encerrar

    print("Saída do comando:\n", container_info.stdout)
    print("Código de retorno:", container_info.retcode)

    assert container_info.retcode == 0
    