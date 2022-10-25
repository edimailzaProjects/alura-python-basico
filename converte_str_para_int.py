print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************")

numero_secreto = 10 # aqui é muito semelhante ao Ruby

chute_str = input("Digite o seu numero: ") # ele vai receber uma string

print ("Você digitou: ", chute_str)

chute = int(chute_str) # aqui converte a string para inteiro, não há conversão instantânea em Python

if (numero_secreto == chute):
    print("Você acertou")
else:
    print("Você errou")

    # sem esse tratamento de string para inteiro, ambas as mensagens seriam exibidas na tela.