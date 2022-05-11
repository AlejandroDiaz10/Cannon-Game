"""
Game: Cannon (May 11th, 2022)
Student 1: Alejandro Díaz Villagómez | A01276769
Student 2: Emiliano Saucedo Arriola | A01659258

Cannon, hitting targets with projectiles.


1. Make the movement speed for the projectile and the balls faster [DONE BY ALEJANDRO]
2. Make the game never end, so that the balls when leaving the window are repositioned.[DONE BY EMILIANO]
"""

from random import randrange
from turtle import *

from freegames import vector

ball = vector(-200, -200)
speed = vector(0, 0)
targets = []


def tap(x, y):
    """Respond to screen tap."""
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 25
        speed.y = (y + 200) / 25


def inside(xy):
    """Return True if xy within screen."""
    return -200 < xy.x < 200 and -200 < xy.y < 200


def draw():
    """Draw ball and targets."""
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()


def move():
    """Move ball and targets."""
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        target.x -= 0.5

    """Speed - Throwing ball."""
    if inside(ball):
        speed.y -= 0.2  # Smaller value = More speed
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

    # Not ending game - When dots go out of the screen (left side), they are relocated (right side)
    for target in targets:
        if not inside(target):
            # return (Deleted line)
            target.x = 200

            
    """Speed - Targets."""
    ontimer(move, 25)  # Smaller value = More speed


setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()
