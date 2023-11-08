import pygame

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

def ruler_picture(country):
    if country == "Sweden":
        background = 'data/pictures/karlxii600x400.jpg'

    elif country == "Denmark":
        background = 'data/pictures/christianVII600x400.jpg'

    elif country == "Rome":
        background = 'data/pictures/alexander_great600x400.jpg'

    return background

def check_user_country(value):
    country = ""

    if value == 1:
        country = "Sweden"

    elif value == 2:
        country = "Denmark"

    elif value == 3:
        country = "Rome"

    return country

def end_turn():
    def click_action():
        print("Turn ended")

    return click_action
