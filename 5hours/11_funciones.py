
# un conjunto de codigo que realiza una tarea especifica
# nos sirve para ordenar el codigo, para no repetir
# con palabra clave: def
# todo el codigo debajo formara parte de la funcion
# ojo la identacion

def saludar_usuario():
  print("Hola usuario!")

# llamar a la funcion, para ejecutar el codigo dentro de la funcion
saludar_usuario()

# orden de ejecucion
print("Bienvenido")
saludar_usuario()
print("ya te podes ir")

# Parametros: información adicional que se le pasa a la funcion
def saludar_usuario(name):
  print("Hola " + name + "!" )

saludar_usuario("Miguel")
saludar_usuario("Pedro")

# más de un parametro
def saludar_usuario(name, age):
  print("Hola " + name + "!, tu tienes " + str(age))

saludar_usuario("Miguel", 15)
saludar_usuario("Pedro", 32)

# Return: valor que devuelve la funcion
# luego de ejecutar devuelve ese valor de la funcion
# por defecto devuelve: none

def cubo_de_numero(numero):
  return numero * numero * numero
  # si pongo algo luedo del return, ya no se ejecutara

print(cubo_de_numero(3))

# guardar el resultado de la funcion en una variable
def cubo_de_numero(numero):
  return numero * numero * numero

resultado = cubo_de_numero(4)
print(resultado)









