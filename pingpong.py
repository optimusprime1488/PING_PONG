import pygame as pg
pg.init()
w = 1080
h = 720
ammount = 1
ammount1 = 0
win = pg.display.set_mode((w,h))
win.fill((20, 247, 228))
image = pg.image.load("galaxy.jpg")
bg = pg.transform.scale(image,(w,h))
pg.display.flip()
pg.display.set_caption('PingPong2players')
icon = pg.transform.scale(pg.image.load('PP.png'),(w,h))
pg.display.set_icon(icon)

class GameSprite(pg.sprite.Sprite):
    def __init__(self,filename,w,h,x,y,speed):
        super().__init__()
        self.image = pg.transform.scale(pg.image.load(filename),(w,h))
        self.speed = speed
        self.filename = filename
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        win.blit(self.image, (self.rect.x,self.rect.y))

class Player1 (GameSprite):
    def update(self,keys_pressed):
        keys = pg.key.get_pressed()
        if keys_pressed[pg.K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        elif keys_pressed[pg.K_DOWN] and self.rect.y < h - h/5:
            self.rect.y += self.speed

class Player2 (GameSprite):
    def update(self,keys_pressed):
        keys = pg.key.get_pressed()
        if keys_pressed[pg.K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        elif keys_pressed[pg.K_s] and self.rect.y < h - h/5:
            self.rect.y += self.speed

class Ball (GameSprite):
    global ammount1
    def init(self):
        self.speed_x = self.speed
        self.speed_y = self.speed
    def update(self):
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x
        if self.rect.y < 0 or self.rect.y > h - h/6.7:
            self.speed_y *= -1
        if self.rect.colliderect(rocket1) or self.rect.colliderect(rocket2):
            self.speed_x *= -1
            ammount1 += 1

ball = Ball('lin.png',w/9,h/9,w-w/1.85,360,5)
ball.init()
rocket1 = Player1('ufo.png',w/6,h/6,w-w/6,360,10)
rocket2 = Player2('ufo.png',w/6,h/6,0,360,10)

def get_finish():
    global finish, text
    if ball.rect.x < 0:
        text = 'Player1 lose'
        finish = True
    if ball.rect.x > w - w/6.7:
        text = 'Player2 lose'
        finish = True

start1 = pg.font.SysFont('arial',100).render("3",True,(255,255,255))
start2 = pg.font.SysFont('arial',100).render("2",True,(255,255,255))
start3 = pg.font.SysFont('arial',100).render("1",True,(255,255,255))
a = pg.font.SysFont('arial',65).render("Очков:" + str(ammount1),True,(255,255,255))
num1 = pg.font.SysFont('arial',65).render("P1",True,(255,255,255))
num2 = pg.font.SysFont('arial',65).render("P2",True,(255,255,255))
finish = False
run = True
clock = pg.time.Clock()
while run:
    
    for e in pg.event.get():
        if e.type == pg.QUIT:
            run = False
    get_finish()
    if not finish:
        if ammount < 60:
            win.blit(bg,(0,0))
            win.blit(start1,(w-w/1.85,360))
            ammount +=1
        elif ammount < 120:
            win.blit(bg,(0,0))
            win.blit(start2,(w-w/1.85,360))
            ammount +=1
        elif ammount < 180:
            ammount +=1
            win.blit(bg,(0,0))
            win.blit(start3,(w-w/1.85,360))
        elif ammount < 240:
            keys_pressed = pg.key.get_pressed()
            win.blit(bg,(0,0))
            win.blit(num1,(w-w/1.15,0))
            win.blit(num2,(w-w/6,0))
            rocket2.update(keys_pressed)
            rocket2.reset()
            rocket1.update(keys_pressed)
            rocket1.reset()
            ball.update()
            ball.reset()
            win.blit(a,(w-w/2,0))
    else:
        win.blit(bg,(0,0))
        label = pg.font.SysFont('arial',65).render(text,True,(255,255,255))
        win.blit(label,(w-w/1.55,h-h/2))


    pg.display.update()
    clock.tick(60)