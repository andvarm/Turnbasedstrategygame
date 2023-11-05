"""Main menu"""
import game
import pygame
import pygame_menu

pygame.init()

def save_user_name(value):
    global user_name
    user_name = value
    print(user_name)

def set_difficulty(value, difficulty):
    print(difficulty)
    pass

def start_the_game():
    game.window()
    pass

def menu():
    surface = pygame.display.set_mode((600, 400))

    menu = pygame_menu.Menu('Imperium Aureum', 600, 400,
    theme=pygame_menu.themes.THEME_BLUE)

    menu.add.text_input('Name: ', default='Karl XII', onchange=save_user_name)
    menu.add.selector('Difficulty: ', [('Hard', 3), ('Medium', 2), ('Easy', 1)], onchange=set_difficulty)
    menu.add.button('Play', start_the_game)
    menu.add.button('Quit', pygame_menu.events.EXIT)
    menu.mainloop(surface)
