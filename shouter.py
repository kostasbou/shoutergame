from pygame import *


window = display.set_mode((700, 500))

mixer.init()
mixer.music.load('space.ogg')
mixer.music.set_volume(0.5)
mixer.music.play()

class GameSprite():
    def __init__(self, player_image, player_x, player_y, speed):
        self.image = transform.scale(image.load(player_image), (65 ,65))

        self.speed = speed 

        self.rect = self.image.get_rect()
        self.rect.x = player_x 
        self.rect.y = player_y

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Hero(GameSprite):
    def move(self):

        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed 

        if keys[K_d] and self.rect.x < 635:
            self.rect.x += self.speed

class Ufo(GameSprite):
    def update(self):
        self.rect.y+= self.speed


hero = Hero("rocket.png", 330, 440, 9)
enemy = Ufo("ufo.png", 65, 65, 7)


background = transform.scale(image.load("galaxy.jpg"), (700, 500))

game = True
clock = time.Clock()
FPS = 60
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False   

       
    
    window.blit(background, (0, 0))
    
    enemy.draw()
    enemy.move()
    
    hero.draw()
    hero.move()
    
    clock.tick(FPS)
    display.update()
