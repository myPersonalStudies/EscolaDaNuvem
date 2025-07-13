# Crie um script em Python que escreva dados em um arquivo CSV. O arquivo CSV deve conter informações de pessoas, com colunas:
# - Nome, Idade e Cidade.

import csv;

def main():

    pessoas = [
        {"Nome": "Ana Silva",      "Idade": 28, "Cidade": "São Paulo"},
        {"Nome": "Bruno Rocha",    "Idade": 35, "Cidade": "Fortaleza"},
        {"Nome": "Carla Menezes",  "Idade": 22, "Cidade": "Curitiba"},
        {"Nome": "Davi Almeida",   "Idade": 41, "Cidade": "Recife"},
    ];

    # ---- 2. Onde vai ser gravado os dados 
    arquivo_csv = "pessoas.csv";

    # ---- 3. Escrita do CSV 
    with open(arquivo_csv, mode="w", newline="", encoding="utf-8") as fp:
        fieldnames = ["Nome", "Idade", "Cidade"];
        writer = csv.DictWriter(fp, fieldnames=fieldnames);

        # cabeçalho
        writer.writeheader();

        # linhas
        writer.writerows(pessoas);

    print(f"Arquivo '{arquivo_csv}' criado com {len(pessoas)} registros de pessoas reais.");

main();