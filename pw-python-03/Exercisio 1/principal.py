import analisa_ficheiro
import json

def main():
    data = {}
    nome_ficheiro = analisa_ficheiro.pede_nome()
    data['calculos'] = []
    data['calculos'].append({
        'linhas': analisa_ficheiro.calcula_linhas(nome_ficheiro),
        'caracters': analisa_ficheiro.calcula_caracteres(nome_ficheiro),
        'maior palavra': analisa_ficheiro.calcula_palavra_comprida(nome_ficheiro),
        'ocorrencias': analisa_ficheiro.calcula_ocorrencia_de_letras(nome_ficheiro)
    })
    nome_ficheiro = analisa_ficheiro.gera_nome(nome_ficheiro)
    
    with open(nome_ficheiro, 'w') as outfile:
        json.dump(data, outfile, indent=2)


if __name__ == '__main__':
    main()
        