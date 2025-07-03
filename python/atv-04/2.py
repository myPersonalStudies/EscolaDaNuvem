# Crie um programa que gera um perfil de usuário aleatório usando a API 'Random User Generator'.
# O programa deve exibir o nome, email e país do usuário gerado.


# TODO: pipx install requests --include-deps, para Linux, mais especificamente Archlinux, caso tenha outro, procure
# TODO: pip install requests, acredito que esse seja para Windows

import requests;

def main():

    url = "https://randomuser.me/api/";
    resposta = requests.get(url);

    # status 200: Deu tudo certo (OK)
    if resposta.status_code == 200:

        dados = resposta.json();
        usuario = dados['results'][0];

        nome = f"{usuario['name']['first']} {usuario['name']['last']}";
        email = usuario['email'];
        pais = usuario['location']['country'];

        print("Perfil do Usuário Random");
        print(f"Nome : {nome}");
        print(f"E-mail : {email}");
        print(f"País : {pais}");
        
    else:
        print("Erro ao acessar a API.");

main();