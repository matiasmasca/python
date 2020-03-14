# $ sudo apt-get install python3-pip
# como tengo varias versiones de python en la misma maquina hay que indicarle a cual instalar
# $ sudo python3.7 -m pip install pygame

import pygame

# Intialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800,600))

# Title and Icon
pygame.display.set_caption



# Game loop
# No corras la app hasta que tengas un evento que pueda cerrar la ventana
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      #apreto el boton de cierre
      running = False

