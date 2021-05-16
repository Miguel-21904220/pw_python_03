from analise_pasta import *

def main():
    pasta = pede_pasta()
    guarda_resultados(pasta)
    faz_grafico_queijos("% de Extensoes", pasta)
    faz_grafico_barras("Numero de Ficheiros", pasta)

if __name__ == '__main__':
    main()
    