#Operadores Aritmeticos
#Los Operadores son:
# + Suma
# - Resta
# * Multiplicacion
# / División
# % modulo - Devuelve el resto de la división
# ** Exponente - Realiza exponencial
# // División baja - Devuelve el entero de la división

a=10
b=20

c=a+b
print("suma es ",c)

c=b-a
print("resta es ",c)
c=a*b
print("multp es ",c)
c=b/a
print("division es ",c)
c=a%b
print("resto de division es ",c)
c=a**b
print("exponencial es ", c)
c=a//3
print("entero es ", c) #devuelve entero (int) y redondeado hacia abajo

tipo_de_dato = type(c)
print(tipo_de_dato)

