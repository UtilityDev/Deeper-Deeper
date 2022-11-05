# theme: Deeper and Depper

from re import I
import pygame
import random
import sys
import math
import random

# initialize pygame
pygame.init()
clock = pygame.time.Clock()

# window properties
TITLE   = "Deeper & Deeper!"
WIDTH   = 1280
HEIGHT  = 720
FPS     = 120
run = True

# gameplay
score = 0

# text
font = pygame.font.SysFont(None, 36)

# screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)

class Player:
    def __init__(self, x, y, speed, radius):
        self.x = x
        self.y = y
        self.speed  = speed
        self.radius = radius

    def draw(self):
        pygame.draw.circle(screen, (255,0,0), (self.x, self.y), self.radius)

    def move(self, amount):
        self.x += amount * self.speed

class Block(object):
    def __init__(self, x, y, color=(0,0,255)):
        self.x = x
        self.y = y
        self.color = color

    def draw(self):
        pygame.draw.rect(screen, self.color, pygame.Rect((self.x, self.y, 80, 20)))

    def move(self, amount):
        self.y += amount
    
    def generate_colors(self):
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# list of blocks
blocks = []
block_speed = 4
max_block_speed = 9.5
total_blocks = 22

# spawn blocks
for x in range(total_blocks):
    blocks.append(Block(random.randint(0,WIDTH),HEIGHT+random.randint(3,750), (random.randint(0,255),random.randint(0,255),random.randint(0,255))))

player = Player(x=WIDTH/2, y=50, speed=5, radius=20) 

# update method
count = 0
def update():
    global count, score
    global objects
    global block_speed, max_block_speed

    pygame.display.update()

    # player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player.move(-0.5)
        if player.x <= -25:
            player.x = WIDTH
    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player.move(0.5)
        if player.x >= WIDTH + 25:
            player.x = 0

    if count < 50:
        count += 1
    else:
        count = 0
        score += 1
        if block_speed < max_block_speed:
            block_speed += 0.05

# draw method
def draw():
    global blocks

    screen.fill((0,0,0))

    # collision detection
    col_rect = pygame.draw.rect(screen, (0,0,255), pygame.Rect(player.x - player.radius, player.y - player.radius, 40, 40))

    player.draw()
    for block in blocks:
        block.draw()
        if block.y >= -50:
            block.move(-block_speed)
        else:
            block.y = HEIGHT + random.randint(0, 500)
            block.generate_colors()

# game loop
while run:
    clock.tick(FPS)

    # method calling
    update()
    draw()

    # text
    fps_text = font.render("FPS: " + str(math.floor(clock.get_fps())), True, (255,255,255))
    score_text = font.render("SCORE: " + str(score), True, (255,255,255))
    speed_text = font.render("SPEED: " + str(round(block_speed, 2)), True, (255,255,255))

    screen.blit(fps_text, (20, 20))
    screen.blit(score_text, (20, 55))
    screen.blit(speed_text, (20, 90))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # exit game on 'ESC' keypress
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()