from pygame import *
from random import *
mixer.init()
fps = 80
clock = time.Clock()

score1 = 0

score2 = 0

win_w = 700
win_h = 500

game = True
finish = False
window = display.set_mode((win_w, win_h))
display.set_caption("sss")

font.init()
font = font.SysFont('Arial',30)



class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_speed2, sizex, sizey):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (sizex, sizey))
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
        
        if keys_pressed[K_s] and self.rect.y < 350:
            self.rect.y+= self.speed
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y-= self.speed

class Player2(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        
        if keys_pressed[K_d] and self.rect.y < 350:
            self.rect.y+= self.speed
        if keys_pressed[K_e] and self.rect.y > 0:
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
            score2 += 1
        if self.rect.x < 1:
            self.speed2*=-1
            score1 +=1
        if sprite.collide_rect(stena1, self) or sprite.collide_rect(stena2, self):
            self.speed2*= -1
        

shar=Enemy("ball.png", 70, 70, 5, 7, 50, 50)
stena1 = Player("r1.png", win_w - (win_w - 25), 350, 10, 10, 35,170)
stena2 = Player2("r1.png", win_w - 50, 350, 10, 10, 35,170)



while game:
    
    for e in event.get():
        if e.type == QUIT:
            game = False  
        elif e.type == KEYDOWN:
            if e.key ==K_SPACE:
               sprite1.fire()
    clock.tick(fps)
    backgrond = window.fill((0, 0, 0))
    


    scor1 = str(score1)
    scor2 = str(score2)

    score11 = font.render(scor1, 1, (180, 1, 1))
    score22 = font.render(scor2, 1, (180, 1, 1))
    shar.update()
    stena1.update()
    stena2.update()
    window.blit(score11, (10, 50))

    window.blit(score22, (80, 50))
   
    stena1.reset()
    stena2.reset()
    shar.reset()
    display.update()
   
