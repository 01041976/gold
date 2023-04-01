#создай игру "Лабиринт"!
from pygame import *

class Wall(sprite.Sprite):
    def __init__ (self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
            
class GameSprite(sprite.Sprite):
    def __init__ (self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        if keys_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < 620:
            self.rect.x += self.speed   
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed  
        if keys_pressed[K_DOWN] and self.rect.y < 425:
            self.rect.y += self.speed          

class Enemy(GameSprite):
    direction = 'left'
    def update(self):
        if self.rect.x <= 470:
            self.direction = 'right'
        if self.rect.x >= win_width - 85:
            self.direction = 'left'
        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed            

font.init()
font = font.Font(None, 70)
win = font.render("You win!", True, (255, 20, 40))
lose = font.render('You lose!', True, (180, 0, 0))

w1 = Wall(50, 0, 50, 40, 10, 10, 400)
w2 = Wall(50, 0, 50, 40, 10, 650, 10)
w3 = Wall(50, 0, 50, 130, 100, 10, 395)
w4 = Wall(50, 0, 50, 130, 100, 90, 10)
w5 = Wall(50, 0, 50, 680, 10, 10, 470)
w6 = Wall(50, 0, 50, 220, 100, 10, 309)
w7 = Wall(50, 0, 50, 310, 100, 10, 395)
w8 = Wall(50, 0, 50, 310, 100, 150, 10)
w9 = Wall(50, 0, 50, 450, 200, 10, 295)
w10 = Wall(50, 0, 50, 450, 200, 150, 10)
w11 = Wall(50, 0, 50, 560, 100, 150, 10)


win_height = 500
win_width = 700
window = display.set_mode((win_width, win_height))
display.set_caption('Game')
background = transform.scale(image.load('background.jpg'), (700, 500))

player = Player('hero.png', 5, win_height - 80, 4)
monster = Enemy('cyborg.png', win_width - 80, 280, 2)
final = GameSprite('treasure.png', win_width - 120, win_height - 80, 0) 

speed = player.speed
run = True
FPS = 60 
finish = False
clock = time.Clock()

mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')

while run:
    keys_pressed = key.get_pressed()

    for i in event.get():
        if i.type == QUIT:
            run = False

    if finish != True:
        window.blit(background, (0, 0))
        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        w7.draw_wall()
        w8.draw_wall()
        w9.draw_wall()
        w10.draw_wall()
        w11.draw_wall()
        player.update()
        monster.update()

        player.reset()
        monster.reset()
        final.reset()
    
    if sprite.collide_rect(player, monster) or sprite.collide_rect(player, w1) or sprite.collide_rect(player, w2)or sprite.collide_rect(player, w3):
        finish = True
        window.blit(lose, (200, 200))
        kick.play()
    if sprite.collide_rect(player, w4) or sprite.collide_rect(player, w5) or sprite.collide_rect(player, w6) or sprite.collide_rect(player, w7):
        finish = True
        window.blit(lose, (200, 200))
        kick.play()
    if sprite.collide_rect(player, w8) or sprite.collide_rect(player, w9) or sprite.collide_rect(player, w10):
        finish = True
        window.blit(lose, (200, 200))
        kick.play()
    if sprite.collide_rect(player, w11):
        finish = True
        window.blit(lose, (200, 200))
        kick.play()

    if sprite.collide_rect(player, final):
        finish = True
        window.blit(win, (200, 200))
        money.play()  

    clock.tick(FPS)
    display.update()