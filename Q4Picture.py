#creator: Kevin
import pygame

from pygame import Color, Rect
from pygame import draw
from pygame import display

SCREEN_SIZE = (500, 500)

pygame.init()

gameDisplay = display.set_mode(SCREEN_SIZE)


gameDisplay.fill(Color('deepskyblue'))

draw.rect(gameDisplay, Color('green'), Rect(0, 400, 500, 100))

#first two x, y then width and height
draw.polygon(gameDisplay, Color('gray2'), [(100, 200), (400, 200), (250, 50)])

draw.rect(gameDisplay, Color('saddlebrown'), Rect(100, 200, 300, 200))
draw.circle(gameDisplay, Color('gold'), (30, 20), 50)
draw.circle(gameDisplay, Color('grey'), (50, 110), 35)
draw.circle(gameDisplay, Color('grey'), (90, 110), 35)
draw.circle(gameDisplay, Color('grey'), (450, 99), 35)
draw.circle(gameDisplay, Color('grey'), (400, 99), 35)

draw.circle(gameDisplay, Color('blue1'), (30, 170), 3)
draw.circle(gameDisplay, Color('blue1'), (45, 170), 3)
draw.circle(gameDisplay, Color('blue1'), (50, 190), 3)
draw.circle(gameDisplay, Color('blue1'), (65, 190), 3)
draw.circle(gameDisplay, Color('blue1'), (30, 210), 3)
draw.circle(gameDisplay, Color('blue1'), (45, 210), 3)

draw.circle(gameDisplay, Color('blue1'), (50, 230), 3)
draw.circle(gameDisplay, Color('blue1'), (65, 230), 3)
draw.circle(gameDisplay, Color('blue1'), (30, 250), 3)
draw.circle(gameDisplay, Color('blue1'), (45, 250), 3)
draw.circle(gameDisplay, Color('blue1'), (50, 270), 3)
draw.circle(gameDisplay, Color('blue1'), (65, 270), 3)

draw.circle(gameDisplay, Color('blue1'), (30, 290), 3)
draw.circle(gameDisplay, Color('blue1'), (45, 290), 3)
draw.circle(gameDisplay, Color('blue1'), (50, 310), 3)
draw.circle(gameDisplay, Color('blue1'), (65, 310), 3)
draw.circle(gameDisplay, Color('blue1'), (30, 330), 3)
draw.circle(gameDisplay, Color('blue1'), (45, 330), 3)

draw.circle(gameDisplay, Color('blue1'), (50, 350), 3)
draw.circle(gameDisplay, Color('blue1'), (65, 350), 3)
draw.circle(gameDisplay, Color('blue1'), (30, 370), 3)
draw.circle(gameDisplay, Color('blue1'), (45, 370), 3)
draw.circle(gameDisplay, Color('blue1'), (50, 390), 3)
draw.circle(gameDisplay, Color('blue1'), (65, 390), 3)
#
draw.circle(gameDisplay, Color('blue1'), (420, 170), 3)
draw.circle(gameDisplay, Color('blue1'), (435, 170), 3)
draw.circle(gameDisplay, Color('blue1'), (440, 190), 3)
draw.circle(gameDisplay, Color('blue1'), (455, 190), 3)
draw.circle(gameDisplay, Color('blue1'), (420, 210), 3)
draw.circle(gameDisplay, Color('blue1'), (435, 210), 3)

draw.circle(gameDisplay, Color('blue1'), (440, 230), 3)
draw.circle(gameDisplay, Color('blue1'), (455, 230), 3)
draw.circle(gameDisplay, Color('blue1'), (420, 250), 3)
draw.circle(gameDisplay, Color('blue1'), (435, 250), 3)
draw.circle(gameDisplay, Color('blue1'), (440, 270), 3)
draw.circle(gameDisplay, Color('blue1'), (455, 270), 3)

draw.circle(gameDisplay, Color('blue1'), (420, 290), 3)
draw.circle(gameDisplay, Color('blue1'), (435, 290), 3)
draw.circle(gameDisplay, Color('blue1'), (440, 310), 3)
draw.circle(gameDisplay, Color('blue1'), (455, 310), 3)
draw.circle(gameDisplay, Color('blue1'), (420, 330), 3)
draw.circle(gameDisplay, Color('blue1'), (435, 330), 3)

draw.circle(gameDisplay, Color('blue1'), (440, 350), 3)
draw.circle(gameDisplay, Color('blue1'), (455, 350), 3)
draw.circle(gameDisplay, Color('blue1'), (420, 370), 3)
draw.circle(gameDisplay, Color('blue1'), (435, 370), 3)
draw.circle(gameDisplay, Color('blue1'), (440, 390), 3)
draw.circle(gameDisplay, Color('blue1'), (455, 390), 3)

display.flip()
input("Press enter to exit")
