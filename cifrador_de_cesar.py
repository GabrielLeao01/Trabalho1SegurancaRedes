import unicodedata
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

caminho_arquivo = 'texto-cifrado.txt'
with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
    texto = arquivo.read()

letras = ler_letras(texto)
letras = remover_acentos(letras)
print(letras)
letras = cifrar_cesar(letras,20)
#letras = decifrar_cesar(letras,17)

salvar_letras(letras, 'texto-decifrado-cesar.txt')
