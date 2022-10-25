print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************")

numero_secreto = 10

chute_str = input("Digite o seu numero: ")

print ("Você digitou: ", chute_str)

chute   = int(chute_str)
acertou = igual = numero_secreto == chute
maior   = numero_secreto > chute

if (acertou):
    print("Você acertou")
elif (maior): #Aqui é o else if
    print("O número é maior")
else:
    print("O numero é menor")

    print("Fim do jogo")