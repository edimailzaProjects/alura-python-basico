import random #preciso importar!!!

print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************")

#numero_secreto = round(random.random() * 10)  #Usando randômicos até 10 e o arredondando com round, mas random,random inicia flutuante
numero_secreto = round(random.randrange(1,10))
total_tentativas = 10

print(numero_secreto)

for rodada in range(1,total_tentativas + 1): #essa forma de escrever é semelhante ao java
    print("Tentativa {} de {} ".format(rodada, total_tentativas))
    chute_str = input("Digite o numero entre 0 e 10: ")
    print ("Você digitou: ", chute_str)
    chute   = int(chute_str)

    if chute > 0 or chute <= 10:
        acertou = numero_secreto == chute
        maior = numero_secreto > chute
        menor = chute < numero_secreto

        if (maior):
            print("O número é maior")
        elif(maior):
            print("O numero é menor")
        else:
            print("Você acertou.")
            break

    else:
        print("Insira um valor válido")
        continue

print("Fim do jogo")