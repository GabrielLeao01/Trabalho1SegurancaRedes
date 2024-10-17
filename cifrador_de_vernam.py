import unicodedata
alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
chaveAleatoria = 'Ik2zwqj'
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

def cifrar_vernam(letras):
    letras_cifradas = []
    for letra in letras:
        if letra in alfabeto:
            indice = alfabeto.index(letra)
            chave = alfabeto.index(chaveAleatoria[letras.index(letra)])
            novo_indice = (indice + chave) % len(alfabeto)
            letras_cifradas.append(alfabeto[novo_indice])
    return letras_cifradas

def decifrar_vernam(letras):
    letras_decifradas = []
    for letra in letras:
        if letra in alfabeto:
            indice = alfabeto.index(letra)
            print(letras.index(letra))
            chave = alfabeto.index(chaveAleatoria[letras.index(letra)])
            novo_indice = (indice - chave) % len(alfabeto)
            letras_decifradas.append(alfabeto[novo_indice])
    return letras_decifradas

def salvar_letras(letras, caminho_arquivo):
    with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
        arquivo.write(''.join(letras))

caminho_arquivo = 'texto-decifrado-vernam.txt'
with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
    texto = arquivo.read()

letras = ler_letras(texto)
letras = remover_acentos(letras)
letras = remover_nao_alfabeto(letras)
print(len(letras))
print(len(alfabeto))
print(len(chaveAleatoria))
#letras = cifrar_vernam(letras)
letras = decifrar_vernam(letras)
print(len(letras))
print(len(alfabeto))
print(len(chaveAleatoria))
salvar_letras(letras, 'texto-decifrado-vernam.txt')
#62