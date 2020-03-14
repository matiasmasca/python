# Bucles For Each - Bucle "Para cada X"

#for x in xrange(1,10):
#  pass

# la variable que se usa despues del for, tendrá el valor
for un_item in "En este conjunto de letras":
  print(un_item)

amigos = ["Juan", "Caren", "Brayan"]
for nombre_amigo in amigos:
  print(nombre_amigo)
print("fin lista \n")

# de 0 a 9, no incluye a 10.
for indice in range(10):
  print(indice)
print("fin del for \n")

# de 3 a 9, no incluye a 10.
for indice in range(3, 10):
  print(indice)
print("fin del for \n")

amigos = ["Juan", "Caren", "Brayan"]
for index in range(len(amigos)):
  print(amigos[index])


# condiciones simples para un elemento dentro del bucle
amigos = ["Juan", "Caren", "Brayan"]
for index in range(len(amigos)):
  if index == 0:
    print("\n")
    print("=== Lista Amigos ===")
#  else:
#    print("")
  print(amigos[index])
print("=== * ===")

