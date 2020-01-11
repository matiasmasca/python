# Classes
# para representar cosas del mundo real no nos alcanza las variables que vimos... numeros, letras, etc.

# Podemos crear un tipo de dato por ejemplo para guardar todo lo refereido a nuestro "Telefono Celular" o en nuestro caso a un personaje de un juego o un jugador

# Alumno.
# podria guardarlo en variables de texto o numericas pero no me alcanza.

class Student:
# todo lo que esta identado es parte de la clase
  def __init__(self, name, carrera, promedio, en_aprobacion):
    # una funcion que inicializa la clase y define de alguna manera que valores tendrá nuestro alumnos
    # le asignamos valores iniciales a esos valores
    self.name = name
    self.carrera = carrera
    self.promedio = promedio
    self.en_aprobacion = en_aprobacion




# Objects
# tomamos esa plantilla de un estudiante y le damos los valores propios de un estudiante del mundo real

# Si lo queremos hacer en otro archivo
# from 25_classes_and_objects import Student # del archivo Student, importar la clase Student

estudiante1 = Student("Jose", "Negocios", 6.8, False)

print(estudiante1)
print(estudiante1.name)
print(estudiante1.promedio)
print(estudiante1.carrera)
print(estudiante1.en_aprobacion)

estudiante2 = Student("Pamela", "Arte", 9.25, True)

# a este proceso de convertir los objetos del mundo real al código a traves de la estructura de la clase se lo llama "Modelar"



class Jugador:
# todo lo que esta identado es parte de la clase
  def __init__(self, apodo, vida, puntos, esta_jugando):
    # una funcion que inicializa la clase y define de alguna manera que valores tendrá nuestro alumnos
    # le asignamos valores iniciales a esos valores
    self.apodo = apodo
    self.vida = vida
    self.puntos = puntos
    self.esta_jugando = esta_jugando


jugador1 = Jugador("Osama", "100", "9999999", True)
jugador2 = Jugador("HombreInvisible", "100", "9999", True)
jugador3 = Jugador("Quesito", "10", "99", False)

print("\n=== RANKING === \n")
print(jugador1.apodo + " - " + jugador1.puntos)
print(jugador2.apodo + " - " + jugador2.puntos)
print(jugador3.apodo + " - " + jugador3.puntos)
print("\n=== * === \n")
