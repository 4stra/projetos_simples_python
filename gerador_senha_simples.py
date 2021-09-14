import random
import sys


def gerador():
    print("\n       GERADOR DE SENHA       \n")

    comprimento = int(input("Digite o comprimento desejado: \n"))

    caracteres = ("abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?\/-_=+")

    print("Senha gerada: ")
    senha = ("".join(random.sample(caracteres, comprimento)))

    print(senha)


def menu():
    print("\nSelecione uma opção: ")
    print("1 - Gerar nova senha")
    print("2 - Sair")

    menu = input("Digite a opção escolhida:\n")
    if (menu == "1"):
        gerador()

    elif (menu == "2"):
        sys.exit(0)

    else:
        print("Opção inválida")


if (__name__ == "__main__"):
    gerador()
    while True:
        menu()