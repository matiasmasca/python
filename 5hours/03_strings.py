
# salto de linea
print("Curso de \nPython")

# Escapar caracteres
print("Curso de \"Python\"")

phrase = "Curso de Python"
print(phrase)

# concatenación
print(phrase + " esta muy bueno")

# funciones.
print(phrase.lower()) # convertir a minusculas
print(phrase.upper()) # convertir a MAYUSCULAS
print(phrase.isupper()) # esta todo en mayusculas?
print(phrase.upper().isupper()) # podemos convinar funciones
print(len(phrase)) # cantidad de caracteres de la cadena
print(phrase[0]) # caracter por indice en la cadena
print(phrase[0] + phrase[6] + phrase[9]) # iniciales por indice en la cadena
print(phrase.index("C"))
print(phrase.replace("Python", "Ruby")) # remplazar una cadena dentro de otra
