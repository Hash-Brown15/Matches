import pygame
pygame.init()

screen=pygame.display.set_mode((600,600))
screen.fill((255,255,255))
pygame.display.update()

block_blast=pygame.image.load("Block Blast.png")
brawl_stars=pygame.image.load("Brawl Stars.png")
clash_royale=pygame.image.load("Clash Royale.png")
minecraft=pygame.image.load("Minecraft.png")

screen.blit(block_blast,(155,100))
screen.blit(brawl_stars,(155,200))
screen.blit(clash_royale,(155,300))
screen.blit(minecraft,(155,400))

font=pygame.font.SysFont("Lao MN",36)
text=font.render("Block Blast",True,(0,0,0))
text1=font.render("Brawl Stars",True,(0,0,0))
text2=font.render("Clash Royale",True,(0,0,0))
text3=font.render("Minecraft",True,(0,0,0))

screen.blit(text,(350,100))
screen.blit(text1,(350,200))
screen.blit(text2,(350,300))
screen.blit(text3,(350,400))

pygame.display.update()
while 1:
    event=pygame.event.poll()
    if event.type==pygame.MOUSEBUTTONDOWN:
        pos=pygame.mouse.get_pos()
        pygame.draw.circle(screen,(0,0,0),(pos),20,0)
        pygame.display.update()
    elif event.type==pygame.MOUSEBUTTONUP:
        pos2=pygame.mouse.get_pos()
        pygame.draw.line(screen,(0,0,0),(pos),(pos2),5)
        pygame.draw.circle(screen,(0,0,0),(pos2),20,0)
        pygame.display.update()