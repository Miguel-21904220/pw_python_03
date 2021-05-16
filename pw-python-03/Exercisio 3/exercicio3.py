import csv
import os

def pede_pasta():
    while True:
        ficheiro = input("Introduza o nome da pasta: ")
        if os.path.isdir(f"{os.getcwd()}\\{ficheiro}"):
            return ficheiro


def calcula_tamanho_pasta(pasta):
    if os.path.isfile(pasta):
        return os.path.getsize(pasta)

    tamanhoPasta = [calcula_tamanho_pasta(os.path.join(pasta, file)) for file in os.listdir(pasta)]
    calculoTamanhoPasta = sum(tamanhoPasta)
    return calculoTamanhoPasta * 9.537 * 0.00000010

def main():
    ficheiro = pede_pasta()
    tamanho = calcula_tamanho_pasta(ficheiro)
    print(f"{tamanho}Mb")

if __name__ == "__main__":
    main()