# Crie um programa que verifique se uma senha é forte. Uma senha forte deve ter pelo menos 8 caracteres e conter pelo menos um número. 
# O programa deve continuar pedindo senhas até que uma válida seja inserida ou o usuário digite 'sair'.

def senha_forte(senha):

    if len(senha) < 8:

        print("A senha deve ter pelo menos 8 caracteres.");
        return False;

    if not any(char.isdigit() for char in senha):

        print("A senha deve conter pelo menos um número.");
        return False;

    return True;

while True:

    senha = input("Digite uma senha forte (ou 'sair' para encerrar): ");

    if senha.lower() == 'sair':
        print("Encerrando o programa.");
        break;

    if senha_forte(senha):
        print("Senha válida e forte!");
        break;
