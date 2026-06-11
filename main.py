from pygame import *

display_1 = 800
display_2 = 800

window = display.set_mode((800,800))
display.set_caption('ping_pong')

bg_c = (128, 128, 128)

timer = time.Clock()
game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.fill(bg_c)

    display.update()
    timer.tick(40)