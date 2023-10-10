# meu_biblioteca.py

def minha_funcao(parametro):
    """
    Esta é uma função de exemplo que utiliza o parâmetro fornecido.

    :param parametro: O parâmetro a ser utilizado na função.
    :type parametro: str
    """
    print(f"Função minha_funcao chamada com o parâmetro: {parametro}")

def main():
    import sys
    if len(sys.argv) != 3:
        print("Uso: meubiblioteca comando1 parametro1")
        sys.exit(1)
    
    comando = sys.argv[1]
    parametro = sys.argv[2]

    if comando == "abert":
        minha_funcao(parametro)
    else:
        print("Comando desconhecido")

if __name__ == "__main__":
    main()
