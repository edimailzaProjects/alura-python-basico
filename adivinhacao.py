# Adiciona complexidade ao jogo

import random

def jogar_adivinhacao():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 100

    print(numero_secreto)
    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1,total_de_tentativas + 1):
        print("Tentativa {} de {} ".format(rodada, total_de_tentativas))
        chute_str = input("Digite o numero entre 0 e 100: ")
        print ("Você digitou: ", chute_str)
        chute   = int(chute_str)

        if chute > 0 and chute < 100:
            acertou = igual = numero_secreto == chute
            maior = numero_secreto > chute
            menor = chute < numero_secreto

            if acertou:
                print("Você acertou")
                print("Você fez {} pontos".format(pontos))
                break

            else:
                if (maior):
                    print("O número é maior")
                elif (menor):
                    print("O numero é menor")

                pontos_perdidos= abs( numero_secreto - chute)
                pontos = pontos - pontos_perdidos

        else:
            print("Insira um valor válido")
            continue

    print("### Fim do jogo ###")


#para poder utilizar, eu preciso chamar o método aqui

if (__name__=="__main__"):
    jogar_adivinhacao()