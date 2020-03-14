# Tipos de numeros y operaciones
print(2)
print(2.0987)
print(-2.0987)

# operaciones
print(3 + 5.4)
print(3 - 5.4)
print(6 / 3)
print(3 * 2)

print(3 * 4 + 5) #17

# orden de los parentesis
print(3 * (4+5)) #27

print(10 % 3) # modulo, devuelve el resto "remainder"

#variables numericas
my_num = 5
print(my_num)

# Funciones
# Conversion.
print(str(my_num))
print(str(my_num) + " es mi numero favorito")
# int
a = int(3.5)
# float
b = float(3.5)
c = float(3.5)

# para saber el tipo podemos usar la funcion type
type(b)

# valor absoluto
my_num = -5
print(abs(my_num))

# Power: Potencia, base y potencia
print(pow(3,2))

# Max
# devuelve el mayor de los dos
print(max(3,6))

print(min(3,6))

# Redondeo.
print(round(3.3))
print(round(3.7))


# Importar otras funciones.
from math import *

print(floor(3.9)) #devuelve el numero más chico más cercano, quita los decimales
print(ceil(3.1)) # "siil" devuelve el numero mayor más cercano,
print(sqrt(36)) # raiz cuadrada



