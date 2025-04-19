import pygame as pg
pg.init()
w = 1080
h = 720
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

class ball (GameSprite):
    pass

ball1 = GameSprite('lin.png',w/9,h/9,w-w/1.85,360,5)
rocket1 = Player1('ufo.png',w/6,h/6,w-w/6,360,10)
rocket2 = Player2('ufo.png',w/6,h/6,0,360,10)




finish = False
run = True
clock = pg.time.Clock()
while run:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            run = False
    
    if not finish:
        keys_pressed = pg.key.get_pressed()
        win.blit(bg,(0,0))
        rocket2.update(keys_pressed)
        rocket2.reset()
        rocket1.update(keys_pressed)
        rocket1.reset()
        ball1.reset()

    pg.display.update()
    clock.tick(60)