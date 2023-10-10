# albert.py

def create_job_type(job_type):
    """
    Esta é uma função para criar jobs.

    :param job_type: O tipo de job a ser criado.
    :type parametro: str
    """
    print(f"Criação de job do tipo {job_type}")

def main():
    import sys
    if len(sys.argv) != 3:
        print("Uso: albert comando parametro1..N")
        sys.exit(1)
    
    comando = sys.argv[1]
    parametro = sys.argv[2]

    if comando == "create":
        create_job_type(parametro)
    else:
        print("Comando desconhecido")

if __name__ == "__main__":
    main()
