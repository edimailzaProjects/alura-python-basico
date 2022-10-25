#Se o usuario acertar de primeira, o jogo deve parar

print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************")

numero_secreto = 10
total_tentativas = 5

for rodada in range(1,total_tentativas):
    print("Tentativa {} de {} ".format(rodada, total_tentativas))
    chute_str = input("Digite o numero entre 0 e 100000: ")
    print ("Você digitou: ", chute_str)
    chute   = int(chute_str)

    if chute > 0 and chute < 100000:
        acertou = igual = numero_secreto == chute
        maior = numero_secreto > chute
        menor = chute < numero_secreto

        if acertou:
            print("Você acertou")
            break

        else:
            if (maior):
                print("O número é maior")
            elif (menor):
                print("O numero é menor")

            rodada = rodada + 1

    else:
        print("Insira um valor válido")
        continue

print("Fim do jogo")