import pygame

Background = 255, 255, 255

def initCanvas(width, height):
  pygame.init()
  pygame.display.set_caption("Greedy Snake")
  return pygame.display.set_mode([width, height])

width = 600
height = 600

screen = initCanvas(width, height)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit(1)

    screen.fill(Background)    
    pygame.display.update()      
