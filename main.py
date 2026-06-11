from pygame import *

display_1 = 800
display_2 = 800

window = display.set_mode((800,800))
display.set_caption('ping_pong')

bg_c = (128, 128, 128)

timer = time.Clock()
game = True

# --- Класс GameSprit
class GameSprite(sprite.Sprite):
    def __init__(self, x,y , widih, height, image_file):
            
            self.image = transform.scale(image.load(image_file), (widih, height))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
                


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.fill(bg_c)

    display.update()
    timer.tick(40)