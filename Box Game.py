import pygame
import random

pygame.init()


#Constants


white = (255,255,255)
black = (0,0,0)
blue = (0,0,255)
FPS = 30
clock = pygame.time.Clock()
gameExit = True
Moves = 100
SMoves = str(Moves)
lead_x = 100
corner_x = 200
lead_y = 350
corner_y = 450
lead_y_change = 0
lead_x_change = 0
x_rand = 500
x_corner_rand = x_rand + 30
y_rand = 400
y_corner_rand = y_rand + 30
score = 0



#Useless function call, but wanted to try it out. Random box has fixed initial value,
#but the main function will randomize the next coordinates


def RandomBox():
    pygame.draw.rect(gameDisplay, blue, [x_rand,y_rand,30,30])

    
#Game window

    
gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('Box Game!')


#Intro


print("Welcome to our Box game! This game has four keys,\nthe up/down and left/right keys.\n"
      "You are to move the white box around to cover the blue boxes to score points.\n"
      "Your goal is to get as many points as possible."
      "\nYou will have 100 moves before the game is over. We hope you have fun!")


#Player has to enter in 'Start' in order to start the game
gameExit == False

while not gameExit:

    for event in pygame.event.get():
        
        if Moves == 0:
            gameExit = True


        #Background screen is white
        gameDisplay.fill(white)


        #Player-controlled Box
        #When player presses arrow keys, the box moves
        
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                lead_y_change = 60
                Moves -= 1
            if event.key == pygame.K_UP:
                lead_y_change = -60
                Moves -= 1
            if event.key == pygame.K_LEFT:
                lead_x_change = -60
                Moves -= 1
            if event.key == pygame.K_RIGHT:
                lead_x_change = 60
                Moves -= 1
        
        #When player lifts up on arrow keys, the box stops momentum
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                lead_y_change = 0
            elif event.key == pygame.K_DOWN:
                lead_y_change = 0
            elif event.key == pygame.K_LEFT:
                lead_x_change = 0
            elif event.key == pygame.K_RIGHT:
                lead_x_change = 0

        #For when the box hits the bounderies, it bounces back onto the window
        
        if lead_y <= 10:
            lead_y_change = 0
            lead_y = 30
            corner_y = 130
        if lead_y >= 500:
            lead_y_change = 0
            lead_y = 480
            corner_y = 580
        if lead_x <= 10:
            lead_x = 20
            lead_x_change = 0
            corner_x = 120
        if lead_x >= 700:
            lead_x_change = 0
            lead_x = 670
            corner_x = 770

        #Box coordinates are updated with every key press
    
        lead_y += lead_y_change
        corner_y += lead_y_change
        lead_x += lead_x_change
        corner_x += lead_x_change

        #Draws the box and the random box

        pygame.draw.rect(gameDisplay, black, [lead_x,lead_y,100,100])
        RandomBox()

        #Randomizes the random box coordinates when the player box hits the random box
        
        if lead_y < y_rand and corner_y > y_corner_rand and lead_x < x_rand and corner_x > x_corner_rand:
            x_rand = random.randint(100, 700)
            y_rand = random.randint(100, 500)
            score = score + 1
            x_corner_rand = x_rand + 30
            y_corner_rand = y_rand + 30

        
        #Updates amount of moves on the caption

        SMoves = str(Moves)
        pygame.display.set_caption('Box Game! ' + SMoves)

        #Updates screen at FPS
        
        pygame.display.update()
        clock.tick((FPS))

        #Game quits after the user is out of moves
        
        if Moves == 0:
            print("\n\nGame Over")
            gameExit = True

        


#Outro
            
pygame.quit()

score = str(score)

print("You got a score of ", score)
input("Thanks for playing our game! Please rerun the program to play again!", )


