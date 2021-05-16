def calcula_linhas(nome_ficheiro):
    try:
        with open('analisa_ficheiro/' + nome_ficheiro, 'r') as file:
            nonempty_lines = [line.strip("\n") for line in file if line != "\n"]
            nlines = len(nonempty_lines)
            return nlines
    except:
        print("ERROR")

def calcula_caracteres(nome_ficheiro):
    try:
        with open('analisa_ficheiro/' + nome_ficheiro, 'r') as file:
            nlines = len(file.read().replace(" ", ""))
            return nlines
    except:
        print("ERROR")
        
def calcula_palavra_comprida(nome_ficheiro):
    try:
        with open('analisa_ficheiro/' + nome_ficheiro, 'r') as file:
            words = file.read().split()
        max_len = len(max(words, key=len))
        
        return [word for word in words if len(word) == max_len]    
    except:
        print("ERROR")

def calcula_ocorrencia_de_letras(nome_ficheiro):
    try:
        with open('analisa_ficheiro/' + nome_ficheiro, 'r') as file:
            from collections import Counter
            counts = Counter(file.read().lower())
            return counts
    except:
        print("ERROR")