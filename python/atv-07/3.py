# Crie um script em Python que leia e escreva dados em um arquivo JSON. O arquivo JSON deve conter informações de uma pessoa, com campos:
# - Nome, Idade e Cidade.

import json

def escrever_json(nome_arquivo, dados):
    """Escreve os dados no arquivo JSON."""
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)
    print(f"\n✅ Dados salvos em '{nome_arquivo}' com sucesso.")

def ler_json(nome_arquivo):
    """Lê os dados do arquivo JSON e retorna como dicionário."""
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            dados = json.load(f)
        return dados
    except FileNotFoundError:
        print(f"❌ Arquivo '{nome_arquivo}' não encontrado.")
        return {}
    except json.JSONDecodeError:
        print(f"❌ Erro ao decodificar o JSON.")
        return {}

def main():
    arquivo = 'pessoa.json'

    # 1. Dados da pessoa (você pode adaptar para entrada do usuário)
    pessoa = {
        "Nome": "Isabela Martins",
        "Idade": 30,
        "Cidade": "Belo Horizonte"
    }

    # 2. Escrever no JSON
    escrever_json(arquivo, pessoa)

    # 3. Ler do JSON
    dados_lidos = ler_json(arquivo)

    # 4. Exibir os dados
    if dados_lidos:
        print("\n📋 Dados da Pessoa:")
        print(f"Nome  : {dados_lidos.get('Nome')}")
        print(f"Idade : {dados_lidos.get('Idade')}")
        print(f"Cidade: {dados_lidos.get('Cidade')}")

main();