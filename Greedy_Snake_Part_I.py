import pygame

Background = 255, 255, 255
LineColor = 0, 0, 0
Green = 0, 255, 0
Red = 255, 0, 0

def initCanvas(width, height):
  pygame.init()
  pygame.display.set_caption("Greedy Snake")
  return pygame.display.set_mode([width, height])

def drawGrid(screen, rows, columns, width, height, gridSize):
  for x in range(columns):
      pygame.draw.line(screen, LineColor, (x * gridSize, 0), (x * gridSize, height))
  for y in range(rows):
      pygame.draw.line(screen, LineColor, (0, y * gridSize), (width, y * gridSize))

def drawSnake(screen, snake, gridSize):
    radius = gridSize // 2
    for section in snake:
        center = ( section[0]*gridSize + radius, section[1]*gridSize + radius)
        pygame.draw.circle(screen, Green, center, radius)

width = 600
height = 600
gridSize = 60
rows = height // gridSize
columns = height // gridSize

screen = initCanvas(width, height)

snake = [(5, 5)]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit(1)

    screen.fill(Background)   
    drawGrid(screen, rows, columns, width, height, gridSize) 
    drawSnake(screen, snake, gridSize)
    pygame.display.update()      
