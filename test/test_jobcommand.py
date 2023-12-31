import pytest
import os
import shutil
import threading
import time
from albert.jobcommands.jobcommand import (
    JobCommand,
    CreateCommand,
    CheckCommand,
    RunCommand,
    DeployCommand,
    load_and_config_parser,
    load_config_json_to_dict
)

from test.docker_utils import *

def test_create_inference_command():
    parser = load_and_config_parser()
    args = parser.parse_args(["create", "inference", "inference_test", '.'])


    create_command = CreateCommand(args)
    create_command.execute()

    inference_config = load_config_json_to_dict('./inference_test/config.json')
    assert inference_config['type'] == 'inference'
    assert inference_config['name'] == 'inference_test'

    shutil.rmtree('inference_test', ignore_errors=True)    

def test_check_inference_command():

    parser = load_and_config_parser()
    args = parser.parse_args(["create", "inference", "inference_test", '.'])
    create_command = CreateCommand(args)
    create_command.execute()

    os.chdir('inference_test')
   
    parser = load_and_config_parser()
    args = parser.parse_args(["check"])

    check_command = CheckCommand(args)
    return_code, output = check_command.execute()
    # codigo de retorno dos testes é 1 (pois o teste falha pois funcoes do template estao vazias)
    assert output.find("test_load_generative_model - NotImplementedError") >= 0
    assert output.find("test_perform_inference - NotImplementedError") >= 0
    os.chdir('../')
    shutil.rmtree('inference_test', ignore_errors=True)


# Função para iniciar o contêiner Docker em uma thread separada
def threaded_run_inference_command(**kwargs):
    container_info = kwargs['container_info']    
    parser = load_and_config_parser()
    args = parser.parse_args(["create", "inference", "inference_test", '.'])
    create_command = CreateCommand(args)
    create_command.execute()
    template_code_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'template_files',
        'inference_code.py'
    )
    try:
        os.chdir('inference_test')

        shutil.copyfile(
            template_code_path, 
            './source/code.py')
    
        parser = load_and_config_parser()
        args = parser.parse_args(["run"])

        run_command = RunCommand(args)
        retcode, stdout = run_command.execute()

        # Agora, 'output' contém a saída do comando como uma string, e 'return_code' contém o código de retorno
        container_info.stdout = stdout
        container_info.retcode = retcode
        assert (container_info.retcode == 0)  # Execução do container criado não deve gerar erro
    except:
        assert False
    os.chdir('../')        
    shutil.rmtree("inference_test", ignore_errors=True)
    assert True




def test_run_inference_command():

    job_type = 'inference'
    job_name = 'inference_test'

     #testa se aplicação está rodando no começo
    assert not is_flask_application_running(job_type,job_name)
    create_thread_to_execute(
        threaded_run_function=threaded_run_inference_command, 
        job_type = 'inference', 
        job_name = 'inference_test',
        is_application_running=is_flask_application_running       

    )
    assert not is_flask_application_running(job_type,job_name)



