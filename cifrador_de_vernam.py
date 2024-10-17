import unicodedata
import sys

alfabeto = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

def remover_acentos(letras):
    letras_sem_acentos = []
    for letra in letras:
        nfkd_form = unicodedata.normalize('NFKD', letra)
        letra_sem_acento = ''.join([c for c in nfkd_form if not unicodedata.combining(c)])
        letras_sem_acentos.append(letra_sem_acento)
    return letras_sem_acentos

def remover_nao_alfabeto(letras):
    letras_filtradas = [letra for letra in letras if letra in alfabeto]
    return letras_filtradas

def ler_letras(texto):
    letras = []
    for letra in texto:
        letras.append(letra)
    return letras
def ler_chave_cripto(chave):
    chave = []
    for letra in texto:
        chave.append(letra)
    return chave

def cifrar_vernam(letras):
    letras_cifradas = []
    for i in range (0,len(letras)):
        if letras[i] in alfabeto:
            indice = alfabeto.index(letras[i])
            chave = alfabeto.index(chave_cripto[i])
            novo_indice = (indice + chave) % len(alfabeto)
            letras_cifradas.append(alfabeto[novo_indice])
    return letras_cifradas

def decifrar_vernam(letras):
    letras_decifradas = []
    for i in range(0,len(letras)):
        if letras[i] in alfabeto:
            indice = alfabeto.index(letras[i])
            chave = alfabeto.index(chave_cripto[i])
            novo_indice = (indice - chave) % len(alfabeto)
            letras_decifradas.append(alfabeto[novo_indice])
    return letras_decifradas

def salvar_letras(letras, caminho_arquivo):
    with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
        arquivo.write(''.join(letras))



print("Insira a chave no formato: vernam -c : cifrar -d : decifrar chave.dat < texto_entrada.txt > texto_saida.txt exemplo:\n  vernam -c chave.dat < texto_aberto.txt > texto_saida.txt")
entrada = input().strip().split()
if  entrada[0] != 'vernam' or entrada[1] not in ['-c', '-d'] or entrada[3] != '<' or entrada[5] != '>':
    print("Entrada inválida. Por favor, siga o formato especificado.")
    sys.exit(1)

modo = entrada[1]
caminho_chave = entrada[2]
caminho_arquivo = entrada[4]
caminho_saida = entrada[6]

with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
    texto = arquivo.read()
letras = ler_letras(texto)

with open(caminho_chave, 'r', encoding='utf-8') as arquivo:
    texto = arquivo.read()
chave_cripto = ler_chave_cripto(texto)
letras = remover_acentos(letras)
letras = remover_nao_alfabeto(letras)

if modo == '-c':
    letras = cifrar_vernam(letras)
elif modo == '-d':
    letras = decifrar_vernam(letras)

salvar_letras(letras, caminho_saida)