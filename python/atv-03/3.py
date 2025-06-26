#3- Conversor de Temperatura
#Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin.
#O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.

temperatura = float(input("Digite a temperatura: "))
unidade_origem = input("Digite a unidade de origem (C, F ou K): ").upper()
unidade_destino = input("Digite a unidade para qual deseja converter (C, F ou K): ").upper()

if unidade_origem == unidade_destino:
    print(f"A temperatura em {unidade_origem} é: {temperatura}°{unidade_origem}")

elif unidade_origem == "C":

    print(f"A temperatura em Celsius é: {temperatura}°C")

    if unidade_destino == "F":
        temperatura = (temperatura * 9/5) + 32
        print(f"A temperatura em Fahrenheit é: {temperatura}°F")

    elif unidade_destino == "K":
        temperatura = temperatura + 273.15
        print(f"A temperatura em Kelvin é: {temperatura}K")

elif unidade_origem == "F":

    print(f"A temperatura em Fahrenheit é: {temperatura}°F")

    if unidade_destino == "C":
        temperatura = (temperatura - 32) * 5/9
        print(f"A temperatura em Celsius é: {temperatura}°C")

    elif unidade_destino == "K":
        temperatura = (temperatura - 32) * 5/9 + 273.15
        print(f"A temperatura em Kelvin é: {temperatura}K")

elif unidade_origem == "K":

    print(f"A temperatura em Kelvin é: {temperatura}K")

    if unidade_destino == "C":
        temperatura = temperatura - 273.15
        print(f"A temperatura em Celsius é: {temperatura}°C")
        
    elif unidade_destino == "F":
        temperatura = (temperatura - 273.15) * 9/5 + 32
        print(f"A temperatura em Fahrenheit é: {temperatura}°F")