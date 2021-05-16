import os
import csv
from matplotlib import pyplot as plt
from numpy import inf

def pede_pasta():
    try:
        nome = input("Introduza o caminho para pasta: ")
        if os.path.isdir(nome) == True:
            return nome
    except:
        print("ERROR")

def faz_calculos(nome_ficheiro):
        data = {}
        for i in os.listdir():
           extension = os.path.splitext(i)[1]
           if not extension in data:
               data[extension] = {'volume': 1, 'quantidade': 1}
           else:
               data[extension]['volume'] += os.path.getsize(i)
               data[extension]['quantidade'] += 1
        
        return dict(data)

def guarda_resultados(nome_ficheiro):
    data = faz_calculos(nome_ficheiro)
    
    with open(nome_ficheiro + '.csv', 'w', newline='') as file:
        campos = ['Extensao', 'Quantidade', 'Tamanho[kByte']
        writer = csv.DictWriter(file, fieldnames=campos)
        writer.writeheader()
        for extention, info in data.items():
                writer.writerow({'Extensao': extention, 'Quantidade' : info['quantidade'], 'Tamanho[kByte': info['volume']})
                

def faz_grafico_queijos(titulo, nome_ficheiro):
    data = faz_calculos(nome_ficheiro)
    lista_valores = []
    for i in data.values():
        lista_valores.append(i['quantidade'])
        
    plt.pie(lista_valores, labels=data.keys(), autopct='%1.0f%%')
    plt.title(titulo)
    plt.show()

def faz_grafico_barras(titulo, nome_ficheiro):
    
    data = faz_calculos(nome_ficheiro)
    lista_valores = []
    for i in data.values():
        lista_valores.append(i['quantidade'])
    
    plt.bar(data.keys(), lista_valores)
    plt.title(titulo)
    plt.show()