preguntas_mensaje = [
  "¿De qué color son las manzanas?\n(a) Rojas/Verdes\n(b) Violetas\n(c) Naranjas\n\n",
  "¿De qué color son las bananas?\n(a) Rojas\n(b) Celeste\n(c) Amarillas\n\n",
  "¿De qué color son las Frutillas?\n(a)Amarillas\n(b) Rojas\n(c) Azules\n\n",
]

# esta clase podria estar en otro archivo... Preguntas.py y luego lo importamos.

class Pregunta:
  def __init__(self, mensaje, respuesta):
    self.mensaje = mensaje
    self.respuesta = respuesta


# array de objetos pregunta

preguntas = [
  Pregunta(preguntas_mensaje[0], "a"),
  Pregunta(preguntas_mensaje[1], "c"),
  Pregunta(preguntas_mensaje[2], "b")
]


# creamos un funcion
def ejecutar_prueba(preguntas):
  puntos = 0
  for pregunta in preguntas:
    respuesta_usuario = input(pregunta.mensaje)
    if respuesta_usuario == pregunta.respuesta:
      puntos += 1
  print("Obtuviste " + str(puntos) + "/" + str(len(preguntas)) + " respuestas correctas.")

ejecutar_prueba(preguntas) # le pasamos la lista de objetos preguntas
