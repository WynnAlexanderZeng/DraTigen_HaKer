import pygame
import sys
pygame.init()
screen = pygame.display.set_mode(flags=pygame.NOFRAME)
pmwidth=pygame.display.Info().current_w
pmheight=pygame.display.Info().current_h
screen.fill((0,0,0))
pygame.display.set_caption('DraTigen HaKer')
close=pygame.image.load('images/close.png')
closet=pygame.image.load('images/closet.png')
bg=pygame.image.load('images/bg2.jpg')
screen.blit(bg,(0,0))
screen.blit(close,(pmwidth-60,0))
while True:
    mousex,mousey=pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or ((pmwidth-60<mousex<pmwidth and 0<mousey<33) and event.type == pygame.MOUSEBUTTONDOWN):
            pygame.quit()
            sys.exit()
        if pmwidth-60<mousex<pmwidth and 0<mousey<33:
            screen.blit(closet,(pmwidth-60,0))
        else:
            screen.blit(close,(pmwidth-60,0))
    pygame.display.flip()
