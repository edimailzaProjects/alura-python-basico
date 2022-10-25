#Laço For
#usamos o range

for rodada in range(1,10):
    print(rodada) #imprime de 1 a 9


for rodada in range(1,10,2): #se eu quiser que vá de 2 e, 2
    print(rodada) # imprime 1, 3, 5, 7, 9

#podemos também escrever sem o range, apesar do range ser mais flexível

for rodada in [1,2,3,4,5]:
    print(rodada)