import pygame, sys, os

# Intialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800,600))
# la pantalla inicia arriba a la izquierda 0,0.

# Caption and Icon
pygame.display.set_caption("Just Another Space Invaders Clone")

icon = pygame.image.load("assets/images/ufo.png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('assets/images/player.png')
playerX = 370
playerY = 480

def player(x,y):
  #blit es dibujar
  # el recurso y luego las coordenadas
  screen.blit(playerImg, (x, y))

# Game loop
# No corras la app hasta que tengas un evento que pueda cerrar la ventana
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      #apreto el boton de cierre
      running = False
      pygame.quit()

  # if keystroke is pressed check whether its right or left
  if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
          playerX += -1
      if event.key == pygame.K_RIGHT:
          playerX += 1


  # RGB color
  screen.fill((0,0,0))

  player(playerX, playerY)
  pygame.display.update()


