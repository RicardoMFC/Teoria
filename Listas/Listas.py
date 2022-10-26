#Métodos para AÑADIR ELEMENTOS A UNA LISTA
#Método APPEND------------
lista=['u','o']    
lista.append('i')

lista2=['h','y','n']
lista.append(lista2)
#Añade todos lo elementos en una lista de listas
lista.append(lista2[1])
#Puedo añadir solo uno si quiero
print(lista)


#Método EXTEND-------------
lista3=['q','e','r','t']
lista3.extend('hola')
print(lista3)
#Guarda cada letra como un caracter 'h', 'o','l', 'a'


#Método INSERT--------------
lista4=['a','b','c','d','f']
lista4.insert(4,'e')
print(lista4)
#Mete en la posición que indicas un elemento y lo desplaza todo un elemento.


#Métodos para ELIMINAR ELEMENTOS DE UNA LISTA
#Método POP
lista5=['a','b','c','d','e']
lista5.pop(0)   #Elimina el elemento de la posición 0.
print(lista5)


#Método REMOVE
lista6=['x','y','z']
lista6.remove('x') #Elimina la 'x'
print(lista6)


#MÉTODO RANGE 
lista7=list(range(0,20,1))   #Me hace una lista de numeros, desde el 0 hasta el 20 de 1 en 1.
print(lista7)




