from pygame import *
font.init()


w = 600
h = 500
mw = display.set_mode((w, h))
display.set_caption('PingPong')
background = transform.scale(image.load('istockphoto-1085032396-170667a.jpg'), (w, h))
run = True
finish = False
FPS = 60
clock = time.Clock()
speedx = 3
speedy = 3


class GameSprite(sprite.Sprite):
    def __init__(self, pimage, x, y, w, h, speed):
        super().__init__()
        self.image = transform.scale(image.load(pimage), (w, h))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_left(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y >= 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 350:
            self.rect.y += self.speed
    def update_right(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y >= 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 350:
            self.rect.y += self.speed


racket1 = Player('racket.png', 5, 200, 50, 150, 5)
racket2 = Player('racket.png', 545, 200, 50, 150, 5)
ball = Player('tenis_ball.png', 250, 200, 50, 50, 5)
font = font.Font(None, 50)
p1w = font.render('Player 1 Win!', True, (0, 255, 0))
p2w = font.render('Player 2 Win!', True, (0, 255, 0))


while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    if finish != True:
        mw.blit(background, (0, 0))
        racket1.reset()
        racket2.reset()
        ball.reset()
        racket1.update_left()
        racket2.update_right()
        ball.rect.x += speedx
        ball.rect.y += speedy
        if ball.rect.y > h - 50 or ball.rect.y < 0:
            speedy *= -1
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speedx *= -1
        if ball.rect.x > w - 50:
            mw.blit(p1w, (200, 230))
            finish = False
        if ball.rect.x < 0:
            mw.blit(p2w, (200, 230))
            finish = False
        
    
    display.update()
    clock.tick(FPS)
