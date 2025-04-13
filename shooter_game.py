from pygame import *
import random


# Инициализация Pygame
font.init()
window = display.set_mode((700, 500))
display.set_caption("Тараканы")
background = transform.scale(image.load("backg.jpg"), (700, 500))
font1 = font.SysFont("Arial", 40)
enemies = sprite.Group()
deadenemies = sprite.Group()
# Переменные для счета
score = 0
unscore = 0

class GameSprite(sprite.Sprite):
    def __init__(self, scale, player_image, player_x, player_y, player_speed_x, player_speed_y):
        super().__init__()
        self.scale = scale
        self.image = transform.scale(image.load(player_image), (self.scale, self.scale))
        self.speedx = player_speed_x
        self.speedy = player_speed_y
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

class DeadEnemy(GameSprite):
    def update(self):
        
        self.speedx -= 1  
        if self.speedx <= 0:
            self.kill()
            
        

class Enemy(GameSprite):
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.y >= 500 or self.rect.x >= 700 or self.rect.x <= 0 or self.rect.y <= 0:
            global unscore
            unscore += 1
            self.reset(2)  

    def reset(self, killer):
        if killer == 1:
            deadenemy = DeadEnemy(50, "spla.png", self.rect.x, self.rect.y, 50, 0)
            deadenemies.add(deadenemy)
        center_x, center_y = 350, 250
        self.rect.x = random.randint(center_x - 100, center_x + 100)
        self.rect.y = random.randint(center_y - 100, center_y + 100)
        nvg = random.choice([1,2,3,4])
        if nvg == 1:
            self.image = transform.scale(image.load("cockroach_right.png"), (self.scale, self.scale))
            self.speedx = random.choice([1,2])
            self.speedy = 0
        elif nvg == 2:
            self.image = transform.scale(image.load("cockroach_left.png"), (self.scale, self.scale))
            self.speedx = random.choice([-1,-2])
            self.speedy = 0
        elif nvg == 3:
            self.image = transform.scale(image.load("cockroach_down.png"), (self.scale, self.scale))
            self.speedy = random.choice([1,2])
            self.speedx = 0
        elif nvg == 4:
            self.image = transform.scale(image.load("cockroach_up.png"), (self.scale, self.scale))
            self.speedy = random.choice([-1,-2])
            self.speedx = 0
# Создание группы тараканов



# Создание тараканов
for _ in range(5):
    nvg = random.choice([1,2,3,4])
    if nvg == 1:
        enemy_image = "cockroach_right.png"
        speed_x = random.choice([1,2])
        speed_y = 0
    elif nvg == 2:
        enemy_image = "cockroach_left.png"
        speed_x = random.choice([-1,-2])
        speed_y = 0
    elif nvg == 3:
        enemy_image = "cockroach_down.png"
        speed_y = random.choice([1,2])
        speed_x = 0
    elif nvg == 4:
        enemy_image = "cockroach_up.png"
        speed_y = random.choice([-1,-2])
        speed_x = 0
    
    
    
    
    enemy = Enemy(50, enemy_image, random.randint(250, 450), random.randint(150, 350), speed_x, speed_y)
    enemies.add(enemy)

# Инициализация часов
clock = time.Clock()
pl = True

# Главный игровой цикл
while pl:
    for e in event.get():
        if e.type == QUIT:
            pl = False
        if e.type == MOUSEBUTTONDOWN:
            mouse_pos = mouse.get_pos()
            for enemy in enemies:
                if enemy.rect.collidepoint(mouse_pos):
                    score += 1
                    enemy.reset(1)  
                    break
                    
    enemies.update()
    deadenemies.update()
    window.blit(background, (0, 0))
    deadenemies.draw(window)

    enemies.draw(window)
    
    
    # Отображение счета
    score_text = font1.render(f"Убито: {score} Пропущенно: {unscore}", True, (0, 0, 0))
    window.blit(score_text, (10, 10))

    display.update()
    clock.tick(30)
