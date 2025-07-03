# Crie um programa que gera uma senha aleatória com o módulo random, utilizando caracteres especiais, 
# possibilitando o usuário a informar a quantidade de caracteres dessa senha aleatória. ​

import random;
import string;

# string.ascii_letters: incluir letras maiúsculas e minúsculas.
# string.digits: incluir números
# string.punctuation: incluir caracteres especiais

def gerar_senha(tamanho):

    caracteres = string.ascii_letters + string.digits + string.punctuation;
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho));

    return senha;

def main():
    
    try:
        tamanho = int(input("Informe a quantidade de caracteres da senha: "));

        if tamanho <= 0:
            print("Por favor, informe um número maior que zero.");

        else:
            senha = gerar_senha(tamanho);
            print("Senha gerada:", senha);

    except ValueError:
        print("Entrada inválida. Digite um número inteiro.");

main();