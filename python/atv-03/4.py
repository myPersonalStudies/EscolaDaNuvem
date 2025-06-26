#4- Verificador de Ano Bissexto

#Faça um programa que determine se um ano inserido pelo usuário é bissexto ou não.
#Um ano é bissexto se for divisível por 4, exceto anos centenários (divisíveis por 100) que não são divisíveis por 400.

try:
    ano = int(input("Digite o ano: "))
    
    # Verifica se o ano é válido (positivo)
    if ano <= 0:
        print("Erro: Digite um ano válido (maior que 0)")
    else:
        # Verifica se é bissexto
        if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
            print("O ano é bissexto")
        else:
            print("O ano não é bissexto")

except ValueError:
    print("Erro: Digite um número válido!")
except KeyboardInterrupt:
    print("\nPrograma interrompido pelo usuário.")
    