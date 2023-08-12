# Questão 2: Faça um programa que solicite ao usuário o ano em que ele nasceu e verifique se o ano é Bissexto ou não e imprima uma mensagem na tela.


def is_bissexto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    else:
        return False

try:
    ano_nascimento = int(input("Digite o ano de nascimento: "))
    if is_bissexto(ano_nascimento):
        print(f"O ano {ano_nascimento} é bissexto.")
    else:
        print(f"O ano {ano_nascimento} não é bissexto.")
except ValueError:
    print("Entrada inválida. Certifique-se de digitar um ano válido.")
