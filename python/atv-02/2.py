#2- Calculadora de Desconto
#Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

#* Nome do produto: "Camiseta"
#* Preço original: R$ 50.00
#* Porcentagem de desconto: 20%
#O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.

nome_do_produto = "Camiseta"
preco_original = 50.00
porcentagem_de_desconto = 20

valor_do_desconto = preco_original * (porcentagem_de_desconto / 100)
preco_final = preco_original - valor_do_desconto

print(f"O valor do desconto é: {valor_do_desconto:.2f}")
print(f"O preço final é: {preco_final:.2f}")