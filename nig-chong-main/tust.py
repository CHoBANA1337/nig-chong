from pygame import *
from random import *
mixer.init()
fps = 80
clock = time.Clock()

game = True
finish = False
window = display.set_mode((700, 500))
display.set_caption("sss")

font.init()
font = font.SysFont('Arial',30)

backgrond = window.fill((0, 0, 0))


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_speed2):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (80, 65))
        self.speed = player_speed
        self.speed2 = player_speed2
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        
        if keys_pressed[K_w] and self.rect.x < 650:
            self.rect.y+= self.speed
        if keys_pressed[K_s] and self.rect.x > 0:
            self.rect.y-= self.speed

class Player2(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        
        if keys_pressed[K_UP] and self.rect.x > 650:
            self.rect.y+= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 0:
            self.rect.y-= self.speed

class Enemy(GameSprite):
    def update(self):
        self.rect.x-=self.speed2
        self.rect.y-=self.speed
        if self.rect.y <= 1:
            self.speed*=-1
        if self.rect.y > 430:
            self.speed*=-1
        if self.rect.x > 690:
            self.speed2*=-1
        if self.rect.x < 1:
            self.speed2*=-1
        

shar=Enemy("ball.png", 70, 70, 5, 5)

while game:

    for e in event.get():
        if e.type == QUIT:
            game = False  
        elif e.type == KEYDOWN:
            if e.key ==K_SPACE:
               sprite1.fire()
    clock.tick(fps)
   


    display.update()
   
    shar.reset()
    shar.update()

