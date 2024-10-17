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

def ler_letras(texto):
    letras = []
    for letra in texto:
        letras.append(letra)
    return letras

def cifrar_cesar(letras, chave):
    letras_cifradas = []
    for letra in letras:
        if letra in alfabeto:
            indice = alfabeto.index(letra)
            novo_indice = (indice + chave) % len(alfabeto)
            letras_cifradas.append(alfabeto[novo_indice])
        else:
            letras_cifradas.append(letra)  
    return letras_cifradas

def decifrar_cesar(letras, chave):
    letras_decifradas = []
    for letra in letras:
        if letra in alfabeto:
            indice = alfabeto.index(letra)
            novo_indice = (indice - chave) % len(alfabeto)
            letras_decifradas.append(alfabeto[novo_indice])
        else:
            letras_decifradas.append(letra)  
    return letras_decifradas

def salvar_letras(letras, caminho_arquivo):
    with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
        arquivo.write(''.join(letras))


print("Insira a chave no formato: cesar -c : cifrar -d : decifrar -k n : valor da chave a ser usada > texto_entrada.txt > texto_saida.txt exemplo:\n  cesar -c -k 10 < texto_aberto.txt > texto_saida.txt")
entrada = input().strip().split()

if  entrada[0] != 'cesar' or entrada[1] not in ['-c', '-d'] or entrada[2] != '-k' or not entrada[3].isdigit() or entrada[4] != '<':
    print(entrada[1],entrada[2],entrada[3],entrada[4],entrada[7])
    print("Entrada inválida. Por favor, siga o formato especificado.")
    sys.exit(1)

modo = entrada[1]
chave = int(entrada[3])
caminho_entrada = entrada[5]
caminho_saida = entrada[7]
with open(caminho_entrada, 'r', encoding='utf-8') as arquivo:
    texto = arquivo.read()

letras = ler_letras(texto)
letras = remover_acentos(letras)
if modo == '-c':
    letras = cifrar_cesar(letras, chave)
elif modo == '-d':
    letras = decifrar_cesar(letras, chave)

salvar_letras(letras, caminho_saida)
