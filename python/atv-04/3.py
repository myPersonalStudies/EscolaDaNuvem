# Desenvolva um programa que consulte informações de endereço a partir de um CEP fornecido pelo usuário, utilizando a API ViaCEP.
# O programa deve exibir o logradouro, bairro, cidade e estado correspondentes ao CEP consultado.

# TODO: pipx install requests --include-deps, para Linux, mais especificamente Archlinux, caso tenha outro, procure
# TODO: pip install requests, acredito que esse seja para Windows

import requests;

def consultar_cep(cep):

    url = f"https://viacep.com.br/ws/{cep}/json/";
    resposta = requests.get(url);

    if resposta.status_code == 200:

        dados = resposta.json();

        if "erro" in dados:
            print("CEP não encontrado.");

        else:
            
            logradouro = dados.get("logradouro", "N/A");
            bairro = dados.get("bairro", "N/A");
            cidade = dados.get("localidade", "N/A");
            estado = dados.get("uf", "N/A");

            print("\nEndereço Encontrado!!!");
            print(f"Logradouro: {logradouro}");
            print(f"Bairro: {bairro}");
            print(f"Cidade: {cidade}");
            print(f"Estado: {estado}");

    else:
        print("Erro na requisição. Tente novamente.");

def main():

    # .strip():  Remover espaços em branco
    cep = input("Digite o CEP (somente números): ").strip();

    if len(cep) == 8 and cep.isdigit():
        consultar_cep(cep);
        
    else:
        print("Não se faça de esperto!! o CEP possui 8 caracteres.");

main();
