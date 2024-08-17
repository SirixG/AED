
#tuplas -> no pueden modificarse

tupla=("Hello World", "finanzas", 5.32, True)

#lista -> se pueden modificar

lista=["Hello World","finanzas", 5.32,True]

lista[3]="GoGo"

#creando un conjunto (set) (no se accede a elementos por indice, no almacena datos duplicados) no tienen un orden fijo - 
# Se pueden redefinir, pero no se pueden modificar 
# Se accede a los elementos por Bucle - son datos desordenados

conjunto={"Alan Dente", 15, True, 12.34, "Hello World"}
print(conjunto)

#Creando un diccionario dict (Clave + Valor) - No tiene un orden (la estructura es "key : value" y separamos con comas)

dict = {
    "nombre": "alan",
    "prof": "finanzas",
    "años": 38,
    "dato_duplicado": 38,
    "Clave":"Valor"
}
print(dict['años'])
