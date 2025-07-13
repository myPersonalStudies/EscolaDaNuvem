# Crie um script em Python que leia um arquivo CSV e exiba os dados na tela. O arquivo CSV deve conter informações de pessoas, com colunas:
# - Nome, Idade e Cidade.

import csv;

def main():
    arquivo_csv = "pessoas.csv";

    try:
        with open(arquivo_csv, mode="r", encoding="utf-8") as fp:
            leitor = csv.DictReader(fp);

            print("\n#--- Lista de Pessoas -------------------------------#");

            for linha in leitor:

                nome = linha.get("Nome", "").strip();
                idade = linha.get("Idade", "").strip();
                cidade = linha.get("Cidade", "").strip();

                print(f"Nome: {nome:14} | Idade: {idade:>2} | Cidade: {cidade}");

    except FileNotFoundError:
        print(f"Erro: Arquivo '{arquivo_csv}' não encontrado.");

    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo: {e}");

main();