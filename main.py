import pygame
import time
import random


pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (155, 0, 0)
green = (45, 168, 55)
blue = (30, 3, 183)
teal = (117, 218, 255)
yellow = (255, 204, 50)
orange = (255, 155, 49)
dark_grey = (81, 81, 81)
dark_green = (35, 130, 42)
dark_purple = (123, 0, 175)

apple_gain = 3
starting_length = 3
self_kill = "True"

snakeBody1 = pygame.image.load("Duel Snakes/snakeBody1.png")
snakeBody2 = pygame.image.load("Duel Snakes/pixil-frame-0 (2) (1).png")
FuelCell = pygame.image.load("Duel Snakes/New_Piskel_1_30x30.png")
snowflake = pygame.image.load("Duel Snakes/snowflake.png")
gameover = pygame.image.load("Duel Snakes/gameover.png")

about = pygame.image.load("Duel Snakes/about.png")
play = pygame.image.load("Duel Snakes/play.png")
quit = pygame.image.load("Duel Snakes/quit.png")
settings = pygame.image.load("Duel Snakes/settings.png")

how_to = pygame.image.load("Duel Snakes/howto.png")

title = pygame.image.load("Duel Snakes/title.png")

about_num = [402, 300, 273, 112, "about"]
play_num = [125, 300, 273, 112, "play"]
settings_num = [125, 416, 273, 112, "settings"]
quit_num = [402, 416, 273, 112, "quit"]
back_num = [10, 560, 90, 30, "back"]
length_num = [296, 189, 210, 18, "length"]
add_num = [177, 265, 448, 18, "add"]
self_num = [337, 340, 130, 18, "self"]
reset_num = [298, 441, 204, 15, "reset"]
fps_num = [303, 116, 132, 18, "fps"]

buttons = [play_num, about_num, settings_num, quit_num, back_num, length_num, add_num, self_num, reset_num, fps_num] 

display_width = 800
display_height = 600


gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Duel Snakes')
img = pygame.image.load('Duel Snakes/snakeHead2 (1).png')
img2 = pygame.image.load('Duel Snakes/pixil-frame-0 (3) (1).png')

img.set_alpha(100)

clock = pygame.time.Clock()

block_size = 20
FPS = 12
direction = "right"
direction2 = "left"

font = pygame.font.SysFont(None, 25)

  
def message_to_screen(msg,color, y_displace=0, x_displace=0):
  textSurf, textRect, = text_objects(msg,color)
  # screen_text = font.render(msg, True, color)
  # gameDisplay.blit(screen_text, [display_width/2, display_height/2])
  textRect.center = (display_width / 2) + x_displace, (display_height / 2) + y_displace
  gameDisplay.blit(textSurf, textRect)

def button():
  for event in pygame.event.get():
    position = pygame.mouse.get_pos()
    pressed = pygame.mouse.get_pressed()
    hit_button = ""
    for number in buttons:
      if position[0] >= number[0] and position[0] <= number[0] + number[2]:
        if position[1] >= number[1] and position[1] <=  number[1] + number[3]:
          if pressed[0] == 1:
            hit_button =  number[4]

    global mcbobber
    mcbobber = hit_button
    return mcbobber

def menu():
  menu_loop = True
  gameDisplay.fill(green)
  gameDisplay.blit(play, (play_num[0], play_num[1]))
  gameDisplay.blit(about, (about_num[0], about_num[1]))
  gameDisplay.blit(settings, (settings_num[0], settings_num[1]))
  gameDisplay.blit(quit, (quit_num[0], quit_num[1]))

  gameDisplay.blit(title, (display_width/2 - 380, 20))
  pygame.display.update()

  while menu_loop:
    global direction
    global direction2
    mcbobber = button()
    if mcbobber == "play":
      direction = "right"
      direction2 = "left"
      gameLoop()
    if mcbobber == "about":
      about_screen()
    if mcbobber == "quit":
      pygame.quit()
    if mcbobber == "settings":
      settings_screen()
    
  
    
    clock.tick(15)

def settings_screen():
  global starting_length
  global apple_gain
  global self_kill
  global FPS
  gameDisplay.fill(green)
  pygame.display.update()
  repeat = True
  message_to_screen("Back", white, 285, -375)
  message_to_screen("Reset to default settings", red, 150)
  message_to_screen("Settings - Click on the setting you want to modify.", red, - 250)
  while repeat:

    pygame.draw.rect(gameDisplay, green, [0, 110, 800, 300])
    message_to_screen("Starting snake length: " + str(starting_length), white, -100)
    message_to_screen("Length added to snake when an apple is consumed: " + str(apple_gain), white, -25)
    message_to_screen("Self - kill: " + self_kill, white, 50)
    message_to_screen("Game FPS: " + str(FPS), white, -175)

    pygame.display.update()

    hit_button = button()
    if hit_button == "back":
      repeat = False
      menu()
    if hit_button == "length":
      starting_length +=1
    if hit_button == "add":
      apple_gain += 1
    if hit_button == "self":
      if self_kill == "False":
        self_kill = "True"
      elif self_kill == "True":
        self_kill = "False"
    if hit_button == "reset":
      self_kill = "True"
      apple_gain = 3
      starting_length = 3
      FPS = 10
    clock.tick(15)
    if hit_button == "fps":
      print("hit")
      FPS += 1
  return
  # pygame.draw.rect(gameDisplay, green, [XnY[0],XnY[1]  ,block_size,block_size]) 

def about_screen():
  repeat = True

  gameDisplay.fill(green)
  message_to_screen("About This Game", white, -275)
  gameDisplay.blit(how_to, (25, 150))
  message_to_screen("Back", white, 285, -375)
  pygame.display.update()

  while repeat:
    hit_button = button()
    if hit_button == "back":
      repeat = False
      menu()
    


def snake(block_size, snakelist):

  if direction == "right":
    head = pygame.transform.rotate(img, 270)
  elif direction == "left":
    head = pygame.transform.rotate(img, 90)
  elif direction == "up":
    head = img
  elif direction == "down":
    head = pygame.transform.rotate(img, 180)

  gameDisplay.blit(head, (snakelist[-1][0], snakelist[-1][1]))

  for XnY in snakelist[:-1]:
    # pygame.draw.rect(gameDisplay, green, [XnY[0],XnY[1]  ,block_size,block_size]) 
    gameDisplay.blit(snakeBody1,(XnY[0],XnY[1]))

def snake2(block_size, snakelist2):

  if direction2 == "right":
    head2 = pygame.transform.rotate(img2, 270)
  if direction2 == "left":
    head2 = pygame.transform.rotate(img2, 90)
  if direction2 == "up":
    head2 = img2
  if direction2 == "down":
    head2 = pygame.transform.rotate(img2, 180)

  gameDisplay.blit(head2, (snakelist2[-1][0], snakelist2[-1][1]))

  for XnY in snakelist2[:-1]:
    gameDisplay.blit(snakeBody2,(XnY[0],XnY[1]))

def text_objects(text,color):
  textSurface = font.render(text, True, color)
  return textSurface, textSurface.get_rect()

def gameLoop():
  global direction
  global direction2
  gameExit = False
  gameOver = False

  lead_x = display_width/2 + 40
  lead_y = display_height/2

  lead_x2 = display_width/2 - 40
  lead_y2 = display_height/2

  lead_x_change = 20
  lead_y_change = 0

  lead_x2 = display_width/2
  lead_y2 = display_height/2

  lead_x_change2 = -20
  lead_y_change2 = 0

  snakeList = [] 
  snakeLength = starting_length

  snakeList2 = [] 
  snakeLength2 = starting_length

  winner = "none"
  
  def relocateX():
    return round(random.randrange(0, display_width-block_size)/20.0)*20.0
  def relocateY():
    return round(random.randrange(0, display_height-60)/20.0)*20.0

  def powerup(lead_x, lead_y, objectX, objectY):
    if lead_x == objectX:
      if lead_y == objectY:
        return True

  randAppleX = relocateX()
  randAppleY = relocateY()

  randAppleX2 = relocateX()
  randAppleY2 = relocateY()

  randSnowX = relocateX()
  randSnowY = relocateY()

  death_anime = True

  slow = False
  iced = False
  icedelay = 0

  slow2 = False
  iced2 = False
  icedelay2 = 0

  ice_spawn = 0

  startDetection = 1

  def draw_background():
    gameDisplay.fill(green)
    x = 0
    repeat = 0
    y = 0
    while repeat < 40:
      pygame.draw.rect(gameDisplay, dark_green, [x-2, 0, 4, 600])
      x += 20
      repeat += 1

    repeat = 0

    while repeat < 30:
      pygame.draw.rect(gameDisplay, dark_green, [0, y-2, 800, 4])
      y += 20
      repeat += 1

  while gameExit == False:

    while gameOver == True:

      #Game Over
      if death_anime == True:
        if winner == "purple":
          draw_background()
          snake2(block_size, snakeList2)
          pygame.display.update()
          time.sleep(0.5)
          snake2(block_size, snakeList2)
          snake(block_size, snakeList)
          pygame.display.update()
          time.sleep(0.5)

          draw_background()
          snake2(block_size, snakeList2)
          pygame.display.update()
          time.sleep(0.5)
          snake2(block_size, snakeList2)
          snake(block_size, snakeList)
          pygame.display.update()
          time.sleep(0.5)

          death_anime = False

        if winner == "green":
          draw_background()
          snake(block_size, snakeList)
          pygame.display.update()
          time.sleep(0.5)
          snake(block_size, snakeList)
          snake2(block_size, snakeList2)
          pygame.display.update()
          time.sleep(0.5)

          draw_background()
          snake(block_size, snakeList)
          pygame.display.update()
          time.sleep(0.5)
          snake(block_size, snakeList)
          snake2(block_size, snakeList2)
          pygame.display.update()
          time.sleep(0.5)

          death_anime = False
      
        if winner == "tie":
          draw_background()
          pygame.display.update()
          time.sleep(0.5)
          snake(block_size, snakeList)
          snake2(block_size, snakeList2)
          pygame.display.update()
          time.sleep(0.5)

          draw_background()
          pygame.display.update()
          time.sleep(0.5)
          snake(block_size, snakeList)
          snake2(block_size, snakeList2)
          pygame.display.update()
          time.sleep(0.5)

          death_anime = False


      gameDisplay.blit(gameover,(0,0))
      message_to_screen("Game over", red,-50)
      message_to_screen("Press C to play again, M to return to the menu, or Q to quit",dark_grey,50 )
      if winner == "purple":
        message_to_screen("Blue Snake Wins!", blue)
      if winner == "green":
        message_to_screen("Yellow Snake Wins!", yellow)
      if winner == "tie":
        message_to_screen("Both players died!", red)
      pygame.display.update()
      for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_q:
            gameExit = True
            gameOver = False
          if event.key == pygame.K_c:
            direction = "right"
            direction2 = "left"
            gameLoop()
          if event.key == pygame.K_m:
            menu()

    #Key Controls
    playerHit = False
    player2Hit = False
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        gameExit = True
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_a:
          if direction != "right":
            if not playerHit:
              lead_x_change = -block_size
              lead_y_change = 0
              direction = "left"
              playerHit = True
        elif event.key == pygame.K_d:
          if direction != "left":
            if not playerHit:
              lead_x_change = block_size
              lead_y_change = 0
              direction = "right"
              playerHit = True
        elif event.key == pygame.K_w:
          if direction != "down":
            if not playerHit:
              lead_y_change = -block_size
              lead_x_change = 0
              direction = "up"
              playerHit = True
        elif event.key == pygame.K_s:
          if direction != "up":
            if not playerHit:
              lead_y_change = block_size
              lead_x_change = 0
              direction = "down"
              playerHit = True
          
        if event.key == pygame.K_LEFT:
          if direction2 != "right":
            if not player2Hit:
              lead_x_change2 = -block_size
              lead_y_change2 = 0
              direction2 = "left"
              player2Hit = True
        if event.key == pygame.K_RIGHT:
          if direction2 != "left":
            if not player2Hit:
              lead_x_change2 = block_size
              lead_y_change2 = 0
              direction2 = "right"
              player2Hit = True
        elif event.key == pygame.K_UP:
          if direction2 != "down":
            if not player2Hit:
              lead_y_change2 = -block_size
              lead_x_change2 = 0
              direction2 = "up"
              player2Hit = True
        elif event.key == pygame.K_DOWN:
          if direction2 != "up":
            if not player2Hit:
              lead_y_change2 = block_size
              lead_x_change2 = 0
              direction2 = "down"
              player2Hit = True

    if not slow:
      lead_x += lead_x_change
      lead_y += lead_y_change

    if not slow2:
      lead_x2 += lead_x_change2
      lead_y2 += lead_y_change2
    
    #Out of Border
    if not slow:
      if lead_x + block_size > display_width:
        lead_x = 0
      elif lead_x < 0:
        lead_x = display_width - block_size

      if lead_y + block_size > display_height - 40: 
        lead_y = 0
      elif lead_y < 0:
        lead_y = display_height - 60
    elif slow == True:
      if lead_x + block_size > display_width:
        lead_x = 40
      elif lead_x < 0:
        lead_x = display_width - 40

      if lead_y + block_size > display_height - 40: 
        lead_y = 20
      elif lead_y < 0:
        lead_y = display_height - 80
      
    if not slow2:
      if lead_x2 + block_size > display_width:
        lead_x2 = 0
      elif lead_x2 < 0:
        lead_x2 = display_width - block_size

      if lead_y2 + block_size > display_height - 40: 
        lead_y2 = 0
      elif lead_y2 < 0:
        lead_y2 = display_height - 60
    elif slow2 == True:
      if lead_x2 + block_size > display_width:
        lead_x2 = 40
      elif lead_x2 < 0:
        lead_x2 = display_width - 40

      if lead_y2 + block_size > display_height - 40: 
        lead_y2 = 20
      elif lead_y2 < 0:
        lead_y2 = display_height - 80

    draw_background()

    pygame.draw.rect(gameDisplay, dark_green, [0, 560, 800, 40])
    message_to_screen("Yellow Snake Length:" + str(snakeLength), yellow, 280, -300)
    message_to_screen("Blue Snake Length:" + str(snakeLength2), blue, 280, 300)

    AppleThickness = 20
    gameDisplay.blit(FuelCell, (randAppleX, randAppleY))
    gameDisplay.blit(FuelCell, (randAppleX2, randAppleY2))
    # pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY, AppleThickness, AppleThickness] )
    if ice_spawn > 450:
      gameDisplay.blit(snowflake, (randSnowX, randSnowY))

    #Snake Head and Body

    if not slow:
      snakeHead = []
      snakeHead.append(lead_x)
      snakeHead.append(lead_y)
      snakeList.append(snakeHead)

    if not slow2:
      snakeHead2 = []
      snakeHead2.append(lead_x2)
      snakeHead2.append(lead_y2)
      snakeList2.append(snakeHead2)
 
    if iced == True:
      if not slow:
        slow = True
      elif slow == True:
        slow = False

    if iced2 == True:
      if not slow2:
        slow2 = True
      elif slow2 == True:
        slow2 = False


    if len(snakeList) > snakeLength:
      del snakeList [0]
    
    if len(snakeList2) > snakeLength2:
      del snakeList2 [0]

    snake(block_size, snakeList)
    snake2(block_size, snakeList2)

    pygame.display.update()

    collission = 1
    collission2 = 1
    while collission <= len(snakeList2):
        if lead_x == snakeList2[collission-1][0]:
            if lead_y  == snakeList2[collission-1][1]:
              winner = "purple"
              while collission2 <= len(snakeList):
                if lead_x2 == snakeList[collission2-1][0]:
                  if lead_y2 == snakeList[collission2-1][1]:
                    winner = "tie"
                    gameOver = True
                    collission2 = len(snakeList) + 1
                    
                collission2 +=1
              if winner == "tie":
                collission = len(snakeList2) + 1
              else:
                gameOver = True
                winner = "purple"
                collission2 = len(snakeList) + 1
                collission = len(snakeList2) + 1
        collission += 1
    
    while collission2 <= len(snakeList):
      if lead_x2 == snakeList[collission2-1][0]:
        if lead_y2 == snakeList[collission2-1][1]:
            winner = "green"
            gameOver = True
            collission2 = len(snakeList) + 1
      collission2 += 1
       
    if self_kill == "True":
      if startDetection == 3:
        collission = 1
        collission2 = 1

        if not slow:
          while collission <= len(snakeList) -1:
            if lead_x == snakeList[collission-1][0]:
                if lead_y  == snakeList[collission-1][1]:
                  while collission2 <= len(snakeList2) -1:
                    if lead_x2 == snakeList2[collission2-1][0]:
                      if lead_y2 == snakeList2[collission2-1][1]:
                        winner = "tie"
                        gameOver = True
                        collission2 = len(snakeList2) + 1
                        
                    collission2 +=1
                  if winner == "tie":
                    collission = len(snakeList) + 1
                  else:
                    gameOver = True
                    winner = "purple"
                    collission2 = len(snakeList2) + 1
                    collission = len(snakeList) + 1
            collission += 1

        
        if not slow2:
          while collission2 <= len(snakeList2) -1:
            if lead_x2 == snakeList2[collission2-1][0]:
              if lead_y2 == snakeList2[collission2-1][1]:
                  winner = "green"
                  gameOver = True
                  collission2 = len(snakeList2) + 1
            collission2 += 1 


      elif startDetection == 1:
        startDetection = 2
      elif startDetection == 2:
        startDetection = 3

    #Apple Collission 

    if powerup(lead_x, lead_y, randAppleX, randAppleY) == True:
      randAppleX = relocateX()
      randAppleY = relocateY()
      snakeLength += apple_gain

    if powerup(lead_x, lead_y, randAppleX2, randAppleY2) == True:
      randAppleX2 = relocateX()
      randAppleY2 = relocateY()
      snakeLength += apple_gain
    
    if powerup(lead_x2, lead_y2, randAppleX, randAppleY) == True:
      randAppleX = relocateX()
      randAppleY = relocateY()
      snakeLength2 += apple_gain

    if powerup(lead_x2, lead_y2, randAppleX2, randAppleY2) == True:
      randAppleX2 = relocateX()
      randAppleY2 = relocateY()
      snakeLength2 += apple_gain
    
    if ice_spawn > 450:
      if powerup(lead_x, lead_y, randSnowX, randSnowY) == True:
        iced2 = True
        slow2 = True
        randSnowX = relocateX()
        randSnowY = relocateY()
        ice_spawn = 0
      
      if powerup(lead_x2, lead_y2, randSnowX, randSnowY) == True:
        iced = True
        slow = True
        randSnowX = relocateX()
        randSnowY = relocateY()
        ice_spawn = 0
    else: ice_spawn += 1


    if iced == True:
      if icedelay <= 120:
        icedelay += 1
      elif icedelay > 120:
        iced = False
        slow = False
        icedelay = 0

    
    if iced2 == True:
      if icedelay2 <= 120:
        icedelay2 += 1
      elif icedelay2 > 120:
        iced2 = False 
        slow2 = False
        icedelay = 0


    clock.tick(FPS)

  pygame.quit()
  quit() 

menu()
#gameLoop()



