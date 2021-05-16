import os
def pede_nome():
    while True:
        try:
            nome_ficheiro = input("Introduza o numero do ficheiro: ")
            with open('analisa_ficheiro/' + nome_ficheiro, 'r') as file:
                return nome_ficheiro
        except:
            print("Nao existe")
            
def gera_nome(x):
    return os.path.splitext(x)[0] + ".json"