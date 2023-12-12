from random import randint



app.stepsPerSecond = 30 #default 30
app.background = 'black'
spaceshipLifeBar = Rect(320, 16, 80, 20, fill='lightblue')
alienLifeBar = Rect(7, 16, 80, 20, fill='lightGreen')
Rect(7, 16, 80, 20, fill=None, border='green', borderWidth=1)
Rect(320, 16, 80, 20, fill=None, border='green', borderWidth=1)

stars = tuple(Star(randint(0, 400), randint(0, 400), randint(2, 4), 4, fill='white') for _ in range(80))
bullets = []

planet = Circle(360, 160, 25, fill=gradient('blue', 'lightBlue', 'blue', 
'skyBlue', 'blue', 'blue', 'lightBlue', 'blue', 'skyBlue', 
'blue', 'blue', 'lightBlue', 'blue', 'skyBlue', 'blue', 'blue', 'lightBlue', 
'blue', 'skyBlue', 'blue', start='left-top'))

sun = Circle(240, -90, 80, fill=gradient('yellow', 'orange'))
winnermessage = Label("YOU WIN", 200 , 200, fill= 'green', size = 80, visible= False)
losermessage = Label("YOU LOSE", 200, 200, fill='red', size= 80, visible= False)

spaceship = Group(
Rect(160, 280, 40, 85, fill='grey'),
Polygon(160, 320, 120, 390, 160, 365, fill='red'),
Polygon(200, 320, 240, 390, 200, 365, fill='red'),
Polygon(160, 280, 180, 240, 200, 280, fill='grey'),
Line(180, 290, 180, 270, fill='red', lineWidth=20),
    
)
#spaceShipTop=Polygon(160, 280, 180, 240, 200, 280, fill='grey'),


spaceship.width *= 0.7
spaceship.height *= 0.7

spaceship.cooldown = 0
spaceship.speed = 12
spaceship.bullets = []

alien = Group(
    Oval(185, 50, 25, 40, fill = 'green'),
    Circle(179, 48, 4),
    Circle(191, 48, 4),
    Line(196, 57, 208, 43, fill= 'green'),
    Line(196, 58, 215, 50, fill= 'green'),
    Line(172, 57, 152, 47, fill= 'green'),
    Line(171, 58, 147, 54, fill= 'green'),
    Circle(184, 71, 40, fill='grey', opacity = 50),
    Oval(185, 85, 120, 50, fill = 'grey')
    )
    
alien.cooldown = 10
alien.speed = 8
alien.bullets = []

moon = Group(
    Circle(50, 100, 30, fill = gradient('black', 'grey', start = 'left')),
    Circle(40, 80, 3, fill= rgb(50, 50, 50)),
    Circle(65, 85, 4, fill = rgb(85, 85, 85)),
    Circle(70, 110, 3, fill = rgb(85, 85, 85)),
    Circle(40, 115, 4, fill = rgb(45, 45, 45)),
    Circle(45, 95, 4, fill = rgb(55, 55, 55)),
    Circle(60, 100, 4, fill = rgb(75, 75, 75)),
    Circle(30, 95, 3, fill = rgb(15, 15, 15)),
    
    
    )

def onKeyHold(keys):
    if 'left' in keys:
        spaceship.left -= spaceship.speed
        if spaceship.left < 0:
            spaceship.left = 0
    if 'right' in keys:
        spaceship.right += spaceship.speed
        if spaceship.right > 400:
            spaceship.right = 400
    if 'space' in keys:
        if spaceship.cooldown <= 0:
            spaceship.bullets.append(Circle(spaceship.centerX, spaceship.top, 5, fill='red'))
            spaceship.cooldown = 8

def onStep():
    for star in stars:
        if star.top>= 400:
            star.bottom = 0
        else:
            star.centerY += star.radius * 3
    if spaceship.cooldown > 0:
        spaceship.cooldown -= 1
    if alien.cooldown > 0:
        alien.cooldown -= 1
    else: #alien.cooldown is 0 (ready to shoot)
        alien.bullets.append(Circle(alien.centerX, alien.bottom, 8, fill= 'lightBlue'))
        alien.cooldown = 10
    for bullet in spaceship.bullets:
        bullet.top -= 15
        if bullet.hitsShape(alien):
            bullet.visible = False
            alienLifeBar.width -= 1
        
        if alienLifeBar.width <= 5:
            winnermessage.visible = True
            alien.cooldown = 10000000000000
            spaceship.cooldown = 10000000000000000
            alien.speed = 0
            alienLifeBar.width = 10
            alienLifeBar.visible = False
    
    for bullet in alien.bullets:
        bullet.bottom += 20
        if bullet.hitsShape(spaceship):
            bullet.visible = False
            spaceshipLifeBar.width -= 1.5
        if spaceshipLifeBar.width <= 5:
            losermessage.visible = True
            alien.cooldown = 1000000000000
            spaceship.cooldown = 100000000000000
            spaceship.speed = 0
            spaceshipLifeBar.width = 10
            spaceshipLifeBar.opacity = 0
    alien.centerX += alien.speed
    planet.centerY += 1
    moon.centerY += 1
    sun.centerY += 1
    if randint(1, 15) == 1 or alien.left <= 0 or alien.right >= 400:
        alien.speed *= -1

Label('Press the arrow keys to move and space to shoot. Goodluck!', 200, 350, size = 10, fill = 'green', bold = True)