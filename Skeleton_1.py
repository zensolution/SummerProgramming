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

def move(snake, direction, columns, rows):
  if direction == 0:
    return snake

  elif direction == 1: #UP
    newX = snake[0][0]
    if snake[0][1] == 0:
      newY = rows - 1
    else:
      newY = snake[0][1] - 1   

  elif direction == 2: #DOWN
    newX = snake[0][0]
    if snake[0][1] == rows - 1:
      newY = 0
    else:
      newY = snake[0][1] + 1    

  elif direction == 3: #LEFT    
    if snake[0][0] == 0:
      newX = columns - 1
    else:
      newX = snake[0][0] - 1   
    newY = snake[0][1]  

  elif direction == 4: #RIGHT    
    if snake[0][0] == columns - 1:
      newX = 0
    else:
      newX = snake[0][0] + 1   
    newY = snake[0][1]  
  
  return (newX, newY)

def changeDirection(key, direction):
  if key == pygame.K_LEFT:
      direction = 3   
  elif key == pygame.K_RIGHT:
      direction = 4
  elif key == pygame.K_UP:
      direction = 1
  elif key == pygame.K_DOWN:
      direction = 2
  return direction

def drawApple(screen, apple, gridSize):
    radius = gridSize // 2
    centerPoint = (apple[0]*gridSize+radius, apple[1]*gridSize+radius)
    pygame.draw.circle(screen, Red, centerPoint, radius)

width = 600
height = 600
gridSize = 60
rows = height // gridSize
columns = height // gridSize
direction = 0 # 1 UP 2 DOWN 3 LEFT 4 RIGHT 0 STOP

screen = initCanvas(width, height)

snake = [(5, 5)]
apple = (2, 2)
clock = pygame.time.Clock()
speed = 3

while True:
    clock.tick(speed)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit(1)
        elif event.type == pygame.KEYDOWN:
          direction = changeDirection(event.key, direction)    

    screen.fill(Background)   
    if direction != 0:   
      newSnakeHead = move(snake, direction, columns, rows)
      snake.insert(0, newSnakeHead)
      snake.remove(snake[len(snake)-1])  
      
    drawGrid(screen, rows, columns, width, height, gridSize) 
    drawSnake(screen, snake, gridSize)
    drawApple(screen, apple, gridSize)

    pygame.display.update()
