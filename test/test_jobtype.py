from albert.jobtypes.jobtype import JobType

def test_jobtype_create():
    # Teste de criação de JobType
    job_type = JobType(name='test_job', type='default')
    destination_folder = 'test_destination'
    try:
        job_type.create(destination_folder)
        assert False, "Método run não gerou exceção"
    except AttributeError:
        pass    

def test_jobtype_run():
    # Teste de execução de JobType
    job_type = JobType(name='test_job', type='default')
    try:
        job_type.run()
        assert False, "Método run não gerou exceção"
    except NotImplementedError:
        pass

def test_jobtype_deploy():
    # Teste de deploy de JobType
    job_type = JobType(name='test_job', type='default')
    try:
        job_type.deploy()
        assert False, "Método deploy não gerou exceção"
    except NotImplementedError:
        pass
