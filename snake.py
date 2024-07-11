import pygame
import time
import random
from pygame.locals import *


class Square(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Square, self).__init__()
        self.surf = pygame.Surface((10, 10)) #represents surface
        self.surf.fill((0, 200, 255)) #fills surface with color
        # self.rect = self.surf.get_rect()
        self.pos = [x, y]


pygame.init()

screen = pygame.display.set_mode((800, 600))
snake_block=10
square = Square(40, 40)
font = pygame.font.SysFont("comicSansms", 40)

def scorer(score):
    value=font.render("Score: "+str(score),True,(255,255,0))
    screen.fill((0, 0, 0), (0, 0, 200, 30))
    screen.blit(value,[0,0])

def our_snake(snake_block, snake_list):
    screen.fill((0,0,0),(0,30,200,600))
    screen.fill((0, 0, 0), (200, 30, 800, 600))
    pygame.draw.rect(screen,(0,255,0),[foodx,foody,snake_block,snake_block])
    for x in snake_list:
        
         pygame.draw.rect(screen, (0,200,255), [x[0], x[1], snake_block, snake_block])

# Use blit to put something on the screen
screen.blit(square.surf, tuple(square.pos))

# Update the display using flip
pygame.display.flip()

font_style = pygame.font.SysFont(None, 50)
def message(msg,color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [350, 250])

gameOn = True
# Our game loop

snake_List=[]
length_snake=1
foodx=round(random.randrange(0,800-snake_block)/10.0)*10.0
foody=round(random.randrange(0,600-snake_block)/10.0)*10.0
while gameOn:
    # for loop through the event queue
    pygame.time.Clock().tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            gameOn = False
    keys = pygame.key.get_pressed()
    # square.surf.fill((0, 0, 0))
    # screen.blit(square.surf, tuple(square.pos)) # Remove old square
    # square.surf.fill((0, 200, 255))
    if keys[K_w] or keys[K_UP]:
        square.pos[1] -= 10
        # keys[K_w] = False
        # keys[K_UP] = False
    if keys[K_a] or keys[K_LEFT]:
        square.pos[0] -= 10
        # keys[K_a] = False
        # keys[K_LEFT] = False
    if keys[K_s] or keys[K_DOWN]:
        square.pos[1] += 10
        # keys[K_s] = False
        # keys[K_DOWN] = False
    if keys[K_d] or keys[K_RIGHT]:
        square.pos[0] += 10
        # keys[K_d] = False
        # keys[K_RIGHT] = False
    if square.pos[0]>=790 or square.pos[0]<0 or square.pos[1]>=590 or square.pos[1]<0:
        gameOn=False
    pygame.draw.rect(screen,(0,255,0),[foodx,foody,snake_block,snake_block])
    snake_head=[]
    snake_head.append(square.pos[0])
    snake_head.append(square.pos[1])
    snake_List.append(snake_head)
    if len(snake_List) > length_snake:
        print(len(snake_List))
        print("p",length_snake)
        del snake_List[0]

    for x in snake_List[:-1] :
        if x==snake_head:
            gameOn=False
    our_snake(snake_block,snake_List)
    scorer(length_snake-1)
    screen.blit(square.surf, tuple(square.pos)) # Put new square
    # Update the display using flip
    pygame.display.flip()

    if square.pos[0] == foodx and square.pos[1]== foody:
            foodx = round(random.randrange(0, 800 - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, 600 - snake_block) / 10.0) * 10.0
            length_snake += 1
    
 
message("Game Over", (255,0,0))
pygame.display.update()
time.sleep(2)
pygame.quit()