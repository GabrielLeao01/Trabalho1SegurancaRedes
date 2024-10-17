from collections import Counter
alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'

def calcular_porcentagem_caracteres(arquivo_entrada, arquivo_saida):
    with open(arquivo_entrada, 'r', encoding='utf-8') as file:
        texto = file.read()
    
    caracteres = [char for char in texto if char in alfabeto]
    total_caracteres = len(caracteres)
    
    contagem = Counter(caracteres)
    
    porcentagens = {caractere: (contagem[caractere] / total_caracteres) * 100 for caractere in contagem}
    
    porcentagens_ordenadas = sorted(porcentagens.items(), key=lambda x: x[1], reverse=True)
    
    with open(arquivo_saida, 'w', encoding='utf-8') as file:
        for caractere, porcentagem in porcentagens_ordenadas:
            file.write(f"'{caractere}': {porcentagem:.2f}%\n")
    print("Análise criptografica salva no arquivo", arquivo_saida)    
print("Insira o nome do arquivo de entrada")
arquivo_entrada = input()
calcular_porcentagem_caracteres(arquivo_entrada, 'saida_criptanalise.txt')
