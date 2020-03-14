
# salto de linea
print("Curso de \nPython")

# Escapar caracteres
print("Curso de \"Python\"")


frase = "Curso de Python"
print(frase)

# concatenación
print(frase + " esta muy bueno")

# funciones para cadenas
print(frase.lower()) # convertir a minusculas
print(frase.upper()) # convertir a MAYUSCULAS
print(frase.isupper()) # esta todo en mayusculas?
print(frase.upper().isupper()) # podemos convinar funciones
print(len(frase)) # cantidad de caracteres de la cadena
print(frase[0]) # caracter por indice en la cadena
print(frase[0] + frase[6] + frase[9]) # iniciales por indice en la cadena
print(frase.index("C"))
print(frase.replace("Python", "Ruby")) # remplazar una cadena dentro de otra
