# Desenvolva uma calculadora em Python que realize as quatro operações básicas (adição, subtração, multiplicação e divisão) entre dois números. A calculadora deve ser capaz de lidar com diversos tipos de erros de entrada e operação. Siga as especificações abaixo:

# A calculadora deve solicitar ao usuário que insira dois números e uma operação.
# As operações válidas são: + (adição), - (subtração), * (multiplicação) e / (divisão).
# O programa deve continuar solicitando entradas até que uma operação válida seja concluída.
# Trate os seguintes erros:
# Entrada inválida (não numérica) para os números
# Divisão por zero
# Operação inválida
# Use try/except para capturar e tratar os erros apropriadamente.
# Após cada erro, o programa deve informar o usuário sobre o erro e solicitar nova entrada.
# Quando uma operação é concluída com sucesso, exiba o resultado e encerre o programa

def obter_numero(mensagem):

    while True:

        try:
            return float(input(mensagem));

        except ValueError:
            print("Erro: Por favor, insira um número válido.");

def obter_operacao():

    while True:
        operacao = input("Digite a operação desejada (+, -, *, /): ");

        if operacao in ['+', '-', '*', '/']:
            return operacao;

        else:
            print("Erro: Operação inválida. Use apenas +, -, * ou /.");

def calcular(n1, n2, operacao):

    try:

        if operacao == '+':
            return n1 + n2;

        elif operacao == '-':
            return n1 - n2;

        elif operacao == '*':
            return n1 * n2;

        elif operacao == '/':
            return n1 / n2;

    except ZeroDivisionError:

        print("Erro: Divisão por zero não é permitida.");
        return None;

while True:

    num1 = obter_numero("Digite o primeiro número: ");
    num2 = obter_numero("Digite o segundo número: ");
    operacao = obter_operacao();

    resultado = calcular(num1, num2, operacao);

    if resultado is not None:
        print(f"Resultado: {num1} {operacao} {num2} = {resultado}");
        break ;
