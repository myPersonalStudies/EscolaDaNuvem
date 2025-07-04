# Crie um programa que solicite ao usuário que insira números inteiros. 
# O programa deve continuar solicitando números até que o usuário digite 'fim'. Para cada número inserido, 
# o programa deve informar se é par ou ímpar. Se o usuário inserir algo que não seja um número inteiro, o programa deve 
# informar o erro e continuar. No final, o programa deve exibir a quantidade de números pares e ímpares inseridos.

pares = 0;
impares = 0;

print("Digite números inteiros. Digite 'fim' para encerrar.");

while True:

    entrada = input("Informe um número inteiro (ou 'fim' para sair): ");

    # Se o usuário digitar 'fim' e derivados ("Fim", "FIM",...), encerra o loop
    # .lower() converte a string para minúsculas para facilitar a comparação
    if entrada.lower() == 'fim':
        break;

    try:

        numero = int(entrada);

        if numero % 2 == 0:
            print(f"{numero} é par.");
            pares += 1;

        else:
            print(f"{numero} é ímpar.");
            impares += 1;

    except ValueError:
        print("Erro: Entrada inválida. Por favor, digite um número inteiro.");

print("\nPrograma encerrado.");
print(f"Quantidade de números pares: {pares}");
print(f"Quantidade de números ímpares: {impares}");

