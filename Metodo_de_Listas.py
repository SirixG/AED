#creando la lista
lista = list(["hola","alan",3])
lista2 = list([1,5,3,10,2,0,False,True])
#devuelve la cantida de elementos de la lista
res = len(lista)

#agregando un elemto a la lista

lista.append("jaja")

#agregando un elemento en una posicion

lista.insert(4,"there")

#agregando varios elementos
lista.extend([False,2030])

#elimintando un elemento de la lista por su indice


lista.pop(-2) #-1 es para eliminar el ultimo, -2 para anteultimo, etc

#removiendo un elemento de la lista por su valor

lista.remove("there")

#eliminando toda la lista 

#lista.clear()

lista2.sort() #False = 0 y True = 1 en el ordenamiento de la lista

lista2.reverse()

print(lista2) 

print(dir(["hola"]))
