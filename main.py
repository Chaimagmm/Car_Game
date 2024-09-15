import pygame
from pygame.locals import *
import random

pygame.init()
running = True
size = width, height =(1200, 600)
# to set the road's width
road_w = int(width/1.6)
roadmark_w = int (width/60)
right_lane = width/2 + road_w/4
left_lane = width/2 - road_w/4
speed = 3

# to determine the dimensions of the screen window
screen = pygame.display.set_mode(size)
# to give it a name
pygame.display.set_caption("Car Game")
# to change the bg color of the screen
screen.fill((60, 220, 0))

# to apply changes
pygame.display.update()
# load the player vehicle
car = pygame.image.load("car.png")
car_loc = car.get_rect()
car_loc.center = right_lane, height*0.7
# load the enemy vehicle
car2 = pygame.image.load("otherCar.png")
car2_loc = car.get_rect()
car2_loc.center = left_lane, height*0.2
counter = 0
while running:
    counter += 1
    if counter == 1024:
        speed += 0.5
        counter = 0
        print("level up")
    # animate the enemy vehicle and  updting the height location to make it moving
    car2_loc[1] += speed
    if car2_loc[1] > height:
        if random.randint(0,1) == 0:
            car2_loc.center = right_lane, -200
        else:
            car2_loc.center = left_lane, -200
    #end game
    if car_loc[0] == car2_loc[0] and car2_loc[1] > car_loc[1] - 250:
        print("GAME OVER! YOU LOST")
        break

    # event listenrs
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key in [K_a, K_LEFT]:
                car_loc = car_loc.move([-int(road_w/2), 0])
            if event.key in [K_d, K_RIGHT]:
                car_loc = car_loc.move([int(road_w/2), 0])
    # drawing the graphics
    # rect means rectangle to draw the road
    pygame.draw.rect(
        screen,
        (50, 50, 50),  # the color
        (width / 2 - road_w / 2, 0, road_w, height)
        # the x and y coordinate : starting with the starting points then the longer
    )
    # drawing the roadmarks
    pygame.draw.rect(
        screen,
        (255, 240, 60),
        (width / 2 - roadmark_w / 2, 0, roadmark_w, height)
    )
    pygame.draw.rect(
        screen,
        (255, 255, 255),
        (width / 2 - road_w / 2 + roadmark_w * 2, 0, roadmark_w, height)
    )
    pygame.draw.rect(
        screen,
        (255, 255, 255),
        (width / 2 + road_w / 2 - roadmark_w * 3, 0, roadmark_w, height)
    )

    screen.blit(car, car_loc)
    screen.blit(car2, car2_loc)
    pygame.display.update()

pygame.quit()
