import kivy
import pygame
from random import randint,choice

#Pygame initialization
pygame.init()
size = (525, 500)#screen size
White = (255, 255, 255) #RGB White

screen = pygame.display.set_mode(size)#screen
screen.fill(White) #screen color

run = True
ls = []
bh = 5
control = []
font = pygame.font.Font(None, 20)
text = 'Restart'
surface = font.render(text, True, (0, 0, 0))
restart = False
loc = (480, 480)

ls2 = []

#loop
while True:
    pygame.display.flip()
    pygame.time.delay(60)
    ship = pygame.image.load("espaco.png")

    screen.blit(ship, (0,0))
    #pygame.time.delay(160)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if x < loc[0] or y < loc[1] or loc[0] != 480:
                ls.insert(len(ls), (x,y, (randint(0, 255), randint(0,255), randint(0,255)), randint(3, 7), 1))
            else:
                restart = True
            
   
    
    for c in range(0,len(ls)):
        if c not in control:
            if ls[c][0] == ls[c][1] and ls[c][1] == 250:
                control.insert(0, c)
                ls2.insert(len(ls2), ((randint(0, 255), randint(0,255), randint(0, 255)), ls[c], randint(3, 7), choice(['-1', '1']), choice(['-1', '1'])))
                bh+=1

        if ls[c][0] != 250 or ls[c][1] != 250:
            pygame.draw.circle(screen, ls[c][2], (ls[c][0],ls[c][1]), ls[c][3])
            
        if (ls[c][0] > 0 - bh and ls[c][0] < 50 - bh) or (ls[c][1] > 0 - bh and ls[c][1] < 50 - bh) or (ls[c][0] > 450 + bh and ls[c][0] < 500 + bh) or (ls[c][1] > 450 + bh and ls[c][0] < 500 + bh):
            v = 0
        else:
            v = ls[c][4]
            '''
            if (ls[c][0] > 250 and ls[c][0] - v < 250) or (ls[c][0] < 250 and ls[c][0] + v > 250):
                val = (250, ls[c][1], ls[c][2], ls[c][3], ls[c][4])
                ls.remove(ls[c])'''
        
        if ls[c][0] < 250:
            if ls[c][0] - 250 > v:
                val = (250, ls[c][1], ls[c][2], ls[c][3], ls[c][4])
                ls.remove(ls[c])
            else:
                val = (ls[c][0] + v, ls[c][1], ls[c][2], ls[c][3], ls[c][4])
                ls.remove(ls[c])
            ls.insert(c, val)
                
        elif ls[c][0] > 250:
            if ls[c][0] - 250 < v:
                val = (250, ls[c][1], ls[c][2], ls[c][3],ls[c][4])
                ls.remove(ls[c])
            else:
                val = (ls[c][0] - v, ls[c][1], ls[c][2], ls[c][3],ls[c][4])
                ls.remove(ls[c])
            ls.insert(c, val)

        if ls[c][1] < 250:
            if ls[c][1] - 250 > v:
                val = (ls[c][0], 250, ls[c][2], ls[c][3],ls[c][4])
                ls.remove(ls[c])
            else:
                val = (ls[c][0], ls[c][1] + v, ls[c][2], ls[c][3], ls[c][4])
                ls.remove(ls[c])
            ls.insert(c, val)
                
        elif ls[c][1] > 250:
            if ls[c][1] - 250 < v:
                val = (ls[c][0], 250, ls[c][2], ls[c][3], ls[c][4])
                ls.remove(ls[c])
            else:
                val = (ls[c][0], ls[c][1] - v, ls[c][2], ls[c][3], ls[c][4])
                ls.remove(ls[c])
            ls.insert(c, val)
        if v != 0:
            val = (ls[c][0], ls[c][1], ls[c][2], ls[c][3], ls[c][4]+1)
            ls.remove(ls[c])
            ls.insert(c, val)
    
    if restart == True:
        if bh == 1:
            if len(ls2) == 0:
                restart = False
            loc = (480, 480)
            for i in ls2:
                ls2.remove(i)
            for c in ls:
                ls.remove(c)
            for d in control:
                control.remove(d)
        else:
            bh -= 1
            loc = (-100, -100)
            for c in range(0, len(ls2)):
                val = (ls2[c][0], (ls2[c][1][0]+randint(2,56)* int(ls2[c][3]), ls2[c][1][1] + randint(2,56) * int(ls2[c][4])),ls2[c][2], ls2[c][3], ls2[c][4])
                ls2.remove(ls2[c])
                ls2.insert(c, val)
        for i in range(0, len(ls2)):
                pygame.draw.circle(screen, (ls2[i][0]), (ls2[i][1]), ls2[i][2])

    if bh > 105:
        if loc[0] != 250:
            loc = (loc[0] -5, loc[1] -5)

    pygame.draw.rect(screen, (255, 0, 0), (loc[0]-2, loc[1]-2, 50, 20))
    screen.blit(surface, loc)
    pygame.draw.circle(screen, (0,0,0), (250,250), bh)

     
    
