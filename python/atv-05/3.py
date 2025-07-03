# Crie uma função que verifique se uma palavra ou frase é um palindromo 
# (lê-se igual de trás para frente, ignorando espaços e pontuação). Se o resultado é True, responda "Sim", 
# se o resultado for False, responda "Não".

import unicodedata
import re

def verificar_palindromo(texto):

    # Remove acentos
    texto_normalizado = unicodedata.normalize('NFD', texto)
    texto_sem_acentos = ''.join(c for c in texto_normalizado if unicodedata.category(c) != 'Mn')

    # Remove pontuação e espaços, e transformar em minúsculas
    texto_limpo = re.sub(r'[^a-zA-Z0-9]', '', texto_sem_acentos).lower()

    # Verifica se é palíndromo
    # texto_limpo[::-1]: de trás pra frente
    if texto_limpo == texto_limpo[::-1]:
        return "Sim"
    else:
        return "Não"

print(verificar_palindromo("Ame a ema"))          # S
print(verificar_palindromo("Socorram-me, subi no ônibus em Marrocos"))  # S
print(verificar_palindromo("teste123 falso"))             # N