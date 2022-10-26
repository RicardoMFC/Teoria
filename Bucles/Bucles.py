#Bucle FOR
letra='a'
letra2='á'
lista=list("La casa de Ángel es azul")

contador=0
for elemento in lista:
    elemento=elemento.lower()
    if letra==elemento or letra2==elemento:
        contador+=1
print(contador)

cont=0
for i, elemento in lista:
    elemento=elemento.lower()
    if elemento[i]==letra:
        cont+=1
print(cont)
