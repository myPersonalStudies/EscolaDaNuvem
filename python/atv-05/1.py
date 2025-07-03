# Crie uma  função que calcule a gorjeta a ser deixada em um restaurante, 
# baseada no valor total da conta e na porcentagem de gorjeta desejada.
# Calcula o valor da gorjeta baseada no total a conta e na porcentagem desejada.

def calcular_gorjeta(valor_conta, porcentagem_gorjeta):

    gorjeta = valor_conta * (porcentagem_gorjeta / 100);
    return gorjeta;

conta = int(input('Digite o valor da conta: '));
porcentagem = int(input('Digite a porcentagem da gorjeta desejada: '));

valor_gorjeta = calcular_gorjeta(conta, porcentagem);
print(f"Gorjeta: R${valor_gorjeta:.2f}");