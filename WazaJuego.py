#pgzero
import random

WIDTH = 1000
HEIGHT = 500
TITLE = "lost fast fly"
FPS = 30

#objetos
fondo1 = Actor("fondo1")
fondo2 = Actor("fondo2")
play = Actor("play",(500,150))
game1 = Actor("game1",(500,250))
eso_wazin1 = Actor("eso_wazin1",(100, 400))
skibidi_1 = Actor("skibidi_1",(980, 400))
skibidi_2 = Actor("skibidi_2",(980, 225))
fondo2 = Actor("fondo2")
go = Actor("GO")
gg = Actor("gg")
enemy = random.randint(1,2)
mode = "menu"
money = 0
count = 0
speed = 5
speed2 = 10
game_over = 0

def skibidis1():
    global count, enemy, speed
    # Movimiento del enemigo: "skibidi_1"
    if skibidi_1.x > -20:
        skibidi_1.x = skibidi_1.x - speed
    else:
        skibidi_1.x = WIDTH + 20
        count = count + 1
        enemy = random.randint(1, 2)
        enemy2 = random.randint(1, 3)
        speed += 1
        
def skibidis2():
    global count, enemy, speed
    # Movimiento del enemigo: "skibidi_toilet"
    if skibidi_2.x > -20:
        skibidi_2.x = skibidi_2.x - speed
    else:
        skibidi_2.x = WIDTH + 20
        count = count + 1
        enemy = random.randint(1, 2)
        enemy2 = random.randint(1, 3)
        speed += 1
        
def draw():
    if mode == "menu":
        fondo2.draw()
        play.draw()
    elif mode == "games":
        fondo2.draw()
        game1.draw()
    elif mode == "game1":
        if count == 0 or count == 1 or count == 2 or count == 3 or count == 4 or count == 5 or count == 6 or count == 7 or count == 8 or count == 9 or count == 10:
            fondo1.draw()
            eso_wazin1.draw()
            screen.draw.text(count, pos=(10, 50), color="white", fontsize = 24)
            if enemy == 1:
                skibidi_1.draw()
            elif enemy == 2:
                skibidi_2.draw()
            screen.draw.text("izi", pos=(10, 30), color="green", fontsize = 24)
            
        elif count == 11 or count == 12 or count == 13 or count == 14 or count == 15 or count == 16 or count == 17 or count == 18 or count == 19 or count == 20:
            fondo1.draw()
            eso_wazin1.draw()
            screen.draw.text(count, pos=(10, 50), color="white", fontsize = 24)
            if enemy == 1:
                skibidi_1.draw()
            elif enemy == 2:
                skibidi_2.draw()
            screen.draw.text("medio", pos=(10, 30), color="yellow", fontsize = 24)
            
        elif count == 21 or count == 22 or count == 23 or count == 24 or count == 25 or count == 26 or count == 27 or count == 28 or count == 29 or count == 30:
            fondo1.draw()
            eso_wazin1.draw()
            screen.draw.text(count, pos=(10, 50), color="white", fontsize = 24)
            if enemy == 1:
                skibidi_1.draw()
            elif enemy == 2:
                skibidi_2.draw()
            screen.draw.text("dificil", pos=(10, 30), color="red", fontsize = 24)
            
        elif count == 31 or count == 32 or count == 33 or count == 34 or count == 35 or count == 36 or count == 37 or count == 38 or count == 39 or count == 40:
            fondo1.draw()
            eso_wazin1.draw()
            screen.draw.text(count, pos=(10, 50), color="white", fontsize = 24)
            if enemy == 1:
                skibidi_1.draw()
            elif enemy == 2:
                skibidi_2.draw()
            screen.draw.text("insano", pos=(10, 30), color="blue", fontsize = 24)
            
        elif count == 41 or count == 42 or count == 43 or count == 44 or count == 45 or count == 46 or count == 47 or count == 48 or count == 49 or count == 50:
            fondo1.draw()
            eso_wazin1.draw()
            screen.draw.text(count, pos=(10, 50), color="white", fontsize = 24)
            if enemy == 1:
                skibidi_1.draw()
            elif enemy == 2:
                skibidi_2.draw()
            screen.draw.text("imposible", pos=(10, 30), color="black", fontsize = 24)
            
    if game_over == 1:
        go.draw()
    elif game_over == 2:
        gg.draw()
            
def update(dt):
    global game_over, count, speed, mode
    
    if enemy == 1:
        skibidis1()
    elif enemy == 2:
        skibidis2()

    #controles
    if mode == "game1" and keyboard.left or keyboard.a and eso_wazin1.x > 20:
        eso_wazin1.x -= 5
        
    elif mode == "game1" and keyboard.right or keyboard.d and eso_wazin1.x > 20:
        eso_wazin1.x += 5
        
        
    if game_over == 1 and keyboard.enter:
        game_over = 0 
        count = 0
        speed = 5
        eso_wazin1.pos = (100, 400)
        skibidi_1.pos = (980, 400)
        skibidi_2.pos = (980, 225)
        
        
    if eso_wazin1.colliderect(skibidi_1) or eso_wazin1.colliderect(skibidi_2):
        game_over = 1
        
    if count == 50:
        game_over = 2
        
def on_mouse_down(button, pos):
    global mode
    #zona de minijuegos+
    if mode == "menu" and button == mouse.LEFT:
        if play.collidepoint(pos):
            mode = "games"
            
    if mode == "games" and button == mouse.LEFT:
        if game1.collidepoint(pos):
            mode = "game1"
        

def on_key_down(key):
    # Salto
    if keyboard.space or keyboard.up or keyboard.w:
        eso_wazin1.y = 200
        animate(eso_wazin1, tween='accelerate', duration=1, y=400)
        