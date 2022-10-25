print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************")

numero_secreto = 10
total_tentativas = 5

for rodada in range(1,total_tentativas): #a variável rodada é declarada aqui e vai até o total de tentativas
    print("Tentativa {} de {} ".format(rodada, total_tentativas)) #interpolação de Strings
    chute_str = input("Digite o seu numero: ")
    print ("Você digitou: ", chute_str)
    chute   = int(chute_str)

    acertou = igual = numero_secreto == chute
    maior   = numero_secreto > chute
    menor = chute < numero_secreto

    if (acertou):
        print("Você acertou")
    else:
        if (maior):
            print("O número é maior")
        elif(menor):
            print("O numero é menor")

    rodada = rodada + 1

print("Fim do jogo")