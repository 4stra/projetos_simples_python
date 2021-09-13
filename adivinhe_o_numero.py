import random
import sys

def adivinha():

    print("*********************************")
    print("      Jogo de Adivinhação!       ")
    print("*********************************")

    numero = random.randrange(0,101)
    tentativa = 0
    
    print("Qual nível de dificuldade?")
    print("(1) Fácil    (2) Normal    (3) Difícil")
    nivel = int(input("Escolha um nível: "))

    if(nivel == 1):
        tentativa = 20

    elif(nivel == 2):
        tentativa = 10

    elif(nivel == 3):
        tentativa = 5

    else:
        print("Escolha entre as três opções disponíveis\n")
        adivinha()



    for rodada in range(1, tentativa + 1):
        print(f"Tentativa {rodada} de {tentativa}")
        chute = int(input("Digite um número entre 1 e 100: \n"))
        print("Você digitou ", chute)
        
        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero
        maior   = chute > numero
        menor   = chute < numero

        if(acertou):
            print(f"Você acertou! O número a ser descoberto era {numero}")
            break

        else:
            if(maior):
                print("Você errou! O seu chute foi maior do que o número a ser descoberto.\n")

            elif(menor):
                print("Você errou! O seu chute foi menor do que o número a ser descoberto.\n")
                
        if (rodada == tentativa):
            print(f"Suas chances se esgotaram! O número a ser descoberto era {numero}.\n")
                
     

def menu():
    print("Selecione uma opção: ")
    print("1 - Jogar novamente")
    print("2 - Sair do jogo")
    menu = input("Digite a opção escolhida:\n")
    if (menu == "1"):
        adivinha()
        
    elif (menu == "2"):
        sys.exit(0)
 
    else : 
        print("Opção inválida")

 

            
    print("Fim de jogo!")
    


if(__name__ == "__main__"):
    adivinha()
    while True:
        menu()