from pygame import*
mixer.init()


class Game_sprite(sprite.Sprite):
    def __init__(self, imagename, width, height, x, y):
        self.image = transform.scale(image.load(imagename),(width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Player(Game_sprite):
    def __init__(self):
        super().__init__("hero.png", 50, 50, 50, 420)




        
        


    def update(self,screen):
        pressed_keys= key.get_pressed()
        if pressed_keys[K_a] and self.rect.x > 0:
            self.rect.x -= 10
        if pressed_keys[K_w] and self.rect.y > 0:
            self.rect.y -= 10
        if pressed_keys[K_d] and self.rect.x < 650:
            self.rect.x += 10
        if pressed_keys[K_s] and self.rect.y < 450:
            self.rect.y += 10





        screen.blit(self.image,self.rect)


        

    def is_collide(self,enemy):
        if self.rect.colliderect(enemy.rect):
            return True
        return False

class Wall(sprite.Sprite):
    def __init__(self,x,y,w,h):
        super().__init__()
        self.image = Surface((w,h))
        self.rect = Rect(x,y,w,h)
        self.image.fill((255,255,255))

    def update(self, screen):
        screen.blit(self.image,self.rect)

class Enemy(Game_sprite):
    def __init__(self):    
        super().__init__("cyborg.png",50,50,460,260)
        self.speed = 3
    def update(self, screen):
        if self.rect.x >= 500:
            self.speed *= -1
        if self.rect.x <= 100:
            self.speed *= -1
        self.rect.x += self.speed


        screen.blit(self.image,self.rect)












window = display.set_mode((700,500))
display.set_caption('Лабиринт')



background = transform.scale(image.load("background.jpg"),(700,500))
win = transform.scale(image.load("aga.jpg"),(700,500))
player = Player()
gold = Game_sprite('treasure.png',250,250,450,200)
lox = transform.scale(image.load("aga1.jpg"),(700,500))
enemy = Enemy()
wall1 = Wall (20,80,20,250)
wall2 = Wall (100,180,20,270)
wall3 = Wall (20,80,350,20)
wall4 = Wall (100,180,350,20)
wall5 = Wall (370,80,300,20)
wall6 = Wall (670,80,20,200)
wall7 = Wall (450,180,20,100)
wall8 = Wall (20,80,20,350)

walls = sprite.Group()
walls.add(wall1)
walls.add(wall2)
walls.add(wall3)
walls.add(wall4)
walls.add(wall5)
walls.add(wall6)
walls.add(wall7)
walls.add(wall8)

mixer.music.load("jungles.ogg")
kick = mixer.Sound('kick.ogg')
mixer.music.play()



clock = time.Clock()
game = True

while game:
    clock.tick(60)
    for e in event.get():
        if e.type == QUIT:
            kick.play()
            game = False
    if player.is_collide(enemy):
        window.blit(lox, (0,0))
    if sprite.spritecollideany(player,walls):
        player.rect.x = 60
        player.rect.y = 420

    window.blit(background,(0,0))
    player.update(window)
    enemy.update(window)
    wall1.update(window)
    wall2.update(window)
    wall3.update(window)
    wall3.update(window)
    wall4.update(window)
    wall5.update(window)
    wall6.update(window)
    wall7.update(window)
    wall8.update(window)

    if player.is_collide(enemy):
        window.blit(lox, (0,0))
    if player.is_collide(gold):
        window.blit(win, (0,0))






    window.blit(gold.image, gold.rect)




    display.update()








