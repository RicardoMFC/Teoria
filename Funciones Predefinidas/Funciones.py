"""FUNCIONES DE CADENAS"""
print('Hola')
print(len('Hola'),"\n")

#Función JOIN--------
lista=['Python','es','us']
lista=''.join(lista)      #Así me uniría todos los caracteres en un único elemento.
print(lista)

lista2=['Python','es','us']
lista2=', '.join(lista2)  #Así me los separa por comas y un espacio.
print(lista2,"\n")


#Función SPLIT---------
cadena="Hola, buenos días"   #Si detecta un espacio, guarda lo que ha leído hasta él, en una posición.
lista3=cadena.split()
print(lista3,"\n")


#Función REPLACE---------
texto="Manuel es mi amigo"
texto=texto.replace('es','era')   #Sustituye el primer elemento indicado por el segundo
print(texto,"\n")


#Función COUNT------------
cadena2="abceabcrabfabc"        #Cuenta cuantas veces se repite "abc" o lo que queramos
print(cadena2.count("abc"))



#Función UPPER-----------
texto2="Hola, qué tal?"
texto2=texto2.upper()
print(texto2,"\n")


#Función LOWER-----------
texto3="ADIOS"
texto3=texto3.lower()
print(texto3,"\n\n")



"""FUNCIONES NUMÉRICAS"""
#Función Range-----------
lista4=list(range(0,5,1))
print(lista4)


#Función STR--------------
lista_aux=[]
c=22
str(c)
lista_aux.append(c)   #Si lo quiero meter en una lista
print(lista_aux,"\n")


#Función INT--------------
j=int(22)
print(type(j))


#Función FLOAT-------------
h=float(9.87)
print(h)


#Función MAX-------------
lista5=list(range(0,10,1))
d=max(lista5)
print(d)


#Función MIN-------------
g=min(lista5)
print(g)


#Función SUM-------------
print(sum(lista5))


"""OTRAS FUNCIONES DE PYTHON"""
x=range(5)

#Función LIST-------------
print(list(x))


#Función TUPLE------------
print(tuple(x))


#Función ORD--------------
s=ord('A')     #Indica la posición del elemento en la tabla ASCII
print(s)


#Función ROUND------------
l=12.867
l=round(l)   #Función que redondea
print(l)


#Función TYPE-------------
v=8
print(type(v))


#Función 

