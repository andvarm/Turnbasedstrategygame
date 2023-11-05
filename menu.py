"""Main menu"""
import game
import pygame
import pygame_menu

"""Initiates pygame"""
pygame.init()

user_name = None
game_difficulty = 3
user_country  = 1

def save_user_name(value):
    """Saves username in variable"""
    global user_name
    user_name = value
    print(user_name)

def save_user_country(index, value):
    global user_country
    user_country = value
    print(value)

def set_difficulty(value, difficulty):
    """Saves difficulty"""
    """3 is hard, 2 is medium and 1 is easy"""
    global game_difficulty
    game_difficulty = difficulty
    print("Game difficulty changed to: ", game_difficulty)
    pass

def start_the_game():
    """Starts the game"""
    print("Game starts with difficulty: ", game_difficulty)
    game.window(game_difficulty, user_country)
    pass

def menu():
    """Menu"""
    surface = pygame.display.set_mode((600, 400))

    menu = pygame_menu.Menu('Imperium Aureum', 600, 400,
    theme=pygame_menu.themes.THEME_BLUE)

    menu.add.text_input('Name: ', default='Karl XII', onchange=save_user_name)
    menu.add.selector('Country: ', [('Sweden', 1), ('Denmark', 2), ('Rome', 3)], onchange=save_user_country)
    menu.add.selector('Difficulty: ', [('Hard', 3), ('Medium', 2), ('Easy', 1)], onchange=set_difficulty)
    menu.add.button('Play', start_the_game)
    menu.add.button('Quit', pygame_menu.events.EXIT)
    menu.mainloop(surface)
