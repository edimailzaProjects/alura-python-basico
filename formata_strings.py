print("*********************************")
print("Interpolação de Strings")
print("*********************************")

#Útil para formatações. Não precisa chamar as Strings ao longo do texto.
print("Tentativa {} de {}".format(3,10))

#Troca o primeiro pelo segundo parâmetro
print("Tentativa {} de {}".format(10,3))

#Imprime flutuante
print("R$ {}".format(1000.64))

#Formata o flutuante impresso (quantos numeros vir antes e depois da virgula
print("R$ {:.2f}".format(1.64))
print("R$ {:.2f}".format(10.64))
print("R$ {:.2f}".format(100.64))
print("R$ {:.2f}".format(1000.64))

#Imprime três primeiros digitos e os dois ultimos, colocando 0 onde falta dígito
print("R$ {:3.2f}".format(1000.6))

 #Formata inteiros e coloca 6 zeros antes dele (isso funciona para flutuantes também)
 #A regra é sempre por zeros na frente
print("R$ {:07d}".format(3))

#Sem o zero
print("R$ {:7.1f}".format(1000.12))

#Formata data
print("Data {:02d}/{:02d}/{:4d}".format(13,10,2022))


#É meu apelido?

print("Edimailza".startswith("Edi"))