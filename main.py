# theme: Deeper and Depper

import pygame
import random
import sys
import math
import random

# initialize pygame
pygame.init()
clock = pygame.time.Clock()

run = True

# window properties
TITLE   = "Deeper & Deeper!"
WIDTH   = 800
HEIGHT  = 600
FPS     = 120

# gameplay 
score = 0

font = pygame.font.SysFont(None, 36)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)

# list of objects
blocks = []

class Player:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self):
        pygame.draw.circle(screen, (255,0,0), (self.x, self.y), self.radius)

    def move(self, amount):
        self.x += amount 

class Block(object):
    def __init__(self, x, y, color=(0,0,255)):
        self.x = x
        self.y = y
        self.color = color

    def draw(self):
        pygame.draw.rect(screen, self.color, pygame.Rect((self.x, self.y, 80, 20)))

    def move(self, amount):
        self.y += amount

player = Player(x=WIDTH/2, y=50, radius=20)

# spawn block
for x in range(15):
    blocks.append(Block(random.randint(0,WIDTH),HEIGHT+random.randint(3,750), (random.randint(0,255),random.randint(0,255),random.randint(0,255))))

# update method
count = 0
def update():
    global count, score
    global objects

    pygame.display.update()

    # player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.move(-5)
        if player.x <= -25:
            player.x = WIDTH
    elif keys[pygame.K_RIGHT]:
        player.move(5)
        if player.x >= WIDTH + 25:
            player.x = 0

    if count < 50:
        count += 1
    else:
        count = 0
        score += 1
        print(score)

# draw method
def draw():
    global blocks

    screen.fill((0,0,0))
    player.draw()
    for block in blocks:
        block.draw()
        if block.y >= -50:
            block.move(-4)
        else:
            block.y = HEIGHT + random.randint(0, 500)

# game loop
while run:
    clock.tick(FPS)

    # method calling
    update()
    draw()

    # text
    fps_text = font.render("FPS: " + str(math.floor(clock.get_fps())), True, (255,255,255))
    score_text = font.render("SCORE: " + str(score), True, (255,255,255))

    screen.blit(fps_text, (20, 20))
    screen.blit(score_text, (20, 55))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # exit game on 'ESC' keypress
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
