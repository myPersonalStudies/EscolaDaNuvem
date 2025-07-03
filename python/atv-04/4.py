# Crie um programa que consulte a cotação atual de uma moeda estrangeira em relação ao Real Brasileiro (BRL). 
# O usuário deve informar o código da moeda desejada (ex: USD, EUR, GBP), e o programa deve exibir o valor atual, 
# máximo e mínimo da cotação, além da data e hora da última atualização.
# Utilize a API da AwesomeAPI para obter os dados de cotação.​

# TODO: pipx install requests --include-deps, para Linux, mais especificamente Archlinux, caso tenha outro, procure
# TODO: pip install requests, acredito que esse seja para Windows

import requests;
from datetime import datetime;

def consultar_cotacao(moeda):

    # .upper(): to Uppercase
    moeda = moeda.upper();
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL";

    resposta = requests.get(url);

    if resposta.status_code == 200:

        dados = resposta.json();
        chave = f"{moeda}BRL";

        if chave in dados:

            info = dados[chave];
            valor = float(info['bid']);
            maximo = float(info['high']);
            minimo = float(info['low']);
            timestamp = int(info['timestamp']);

            data_hora = datetime.fromtimestamp(timestamp).strftime("%d/%m/%Y %H:%M:%S");

            print(f"\nCotação {moeda}/BRL");
            print(f"Valor atual : R$ {valor:.2f}");
            print(f"Valor máximo: R$ {maximo:.2f}");
            print(f"Valor mínimo: R$ {minimo:.2f}");
            print(f"Última atualização: {data_hora}");

        else:
            print("Moeda não encontrada.");

    else:
        print("Erro ao consultar a API.");

def main():

    # .strip(): Remover espaços em branco
    codigo_moeda = input("Informe o código da moeda (ex: USD, EUR, GBP): ").strip();

    #  isalpha(): Verifica se todos os caracteres são letras do alfabeto (A–Z ou a–z), sem números, espaços ou símbolos.
    if codigo_moeda.isalpha() and len(codigo_moeda) == 3:
        consultar_cotacao(codigo_moeda);

    else:
        print("Código inválido. Use um código de 3 letras, como USD, EUR, GBP...");

main();