import pygame
import time
import random as r

pygame.init()       #initialize

white= (255,255,255)  #colors
black=(0,0,0)
c1=(23,235,235)
red=(255,10,10)
green=(0,255,0)
blue=(0,0,220)
disp_width=800
disp_ht=600
gameDisplay= pygame.display.set_mode((disp_width,disp_ht))
pygame.display.set_caption('Infinite Snake')         

img=pygame.image.load('snake1.png')

clock = pygame.time.Clock()            #clock for movement of snake

bsize=10

fps=20   #SPEED

smallfont=pygame.font.SysFont("comicsansms",25)         #text sizes
medfont=pygame.font.SysFont("comicsansms",40)
largefont=pygame.font.SysFont("comicsansms",80)

def pause():                                            #pause game screen
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False

                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        gameDisplay.fill(white)
        msg("PAUSED" ,blue, -100, size = 'large')
        msg("Press C - continue or Q - Quit!!",black,25)
        pygame.display.update()
        clock.tick(5)

def score(score):                                 
    text = smallfont.render("SCORE : " +str(score),True, white)
    gameDisplay.blit(text, [0,0])        #blit-draw one image onto another
    
def game_intro():
    intro=True
    while intro:

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_p:
                    intro=False
                if event.key==pygame.K_q:
                    pygame.quit()
                    quit()

        
        gameDisplay.fill(white)
        msg("Infinite Snake",blue,-100,"large")
        msg("Press P - play or Q - Quit!!",black,120,"medium")

        pygame.display.update()
        clock.tick(15)

def text_objects(text,color,size):
    if size=='small':
        textSurface=smallfont.render(text,True,color)
    elif size=='medium':
        textSurface=medfont.render(text,True,color)
    elif size=='large':
        textSurface=largefont.render(text,True,color)

    return textSurface,textSurface.get_rect()

def msg(m,color,y_disp=0,size="small"):            #position of text
    textSurf,textRect=text_objects(m,color,size)
    #stxt= font.render(m,True,color)
    #gameDisplay.blit(stxt,[50,300])
    textRect.center=(disp_width/2),(disp_ht/2)+y_disp
    gameDisplay.blit(textSurf,textRect)

def snake(bsize,snakeList):
    gameDisplay.blit(img, (snakeList[-1][0],snakeList[-1][1]))
    for xny in snakeList:         #body of snake
        pygame.draw.rect(gameDisplay, green, [xny[0],xny[1],bsize,bsize])
        
        
def gameloop():               #event handling for the game
    gameExit=False
    gameOver=False
    
    lead_x=disp_width/2
    lead_y=disp_ht/2
    lead_xc=0
    lead_yc=0

    Athick=20      #apple thickness
    snakeList = []
    slen = 1
    randAppleX= round(r.randrange(0,disp_width-bsize)/10.0)*10.0  #apple at random position
    randAppleY= round(r.randrange(0,disp_ht-bsize)/10.0)*10.0
    while not gameExit:
        while gameOver==True:
            gameDisplay.fill(black)
            msg("GAME OVER!!!",red,y_disp=-50,size="large")
            msg("PRESS C - CONTINUE or Q - QUIT",white,50,size="medium")
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:    #cross button
                    gameExit = True
                    gameOver = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit=True
                        gameOver=False
                    if event.key == pygame.K_c:
                        gameloop()
                        
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:    #close game window
                gameExit=True
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        lead_xc= -bsize
                        lead_yc=0
                    elif event.key == pygame.K_RIGHT:
                        lead_xc= bsize
                        lead_yc=0
                    elif event.key == pygame.K_UP:
                        lead_yc= -bsize
                        lead_xc=0
                    elif event.key == pygame.K_DOWN:
                        lead_yc= bsize
                        lead_xc=0

                    elif event.key == pygame.K_p:
                        pause()

        
        if lead_x >= disp_width or lead_x< 0 or lead_y>= disp_ht or lead_y<0:
            gameOver=True          #game over if it touches the boundaries
        
        lead_x +=lead_xc           #movement of snake 
        lead_y +=lead_yc
        
        gameDisplay.fill(black)       #background color
        Athick=20
        pygame.draw.rect(gameDisplay,red,[randAppleX,randAppleY,Athick,Athick])

        
        snakeHead = []                      #creating body of snake
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)
        snake(bsize,snakeList)

        if len(snakeList) > slen:
            del snakeList[0]


        score(slen-1)
        pygame.display.update()


        if lead_x>= randAppleX and lead_x<= randAppleX + Athick:            #eating apple
            if lead_y>= randAppleY and lead_y<= randAppleY + Athick:
                randAppleX= round(r.randrange(0,disp_width-bsize)/10.0)*10.0
                randAppleY= round(r.randrange(0,disp_ht-bsize)/10.0)*10.0
                slen+=1    
            

        clock.tick(fps)

   
    pygame.quit()
    quit()          #close shell
game_intro()
gameloop()
