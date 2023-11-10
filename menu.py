"""Main menu"""
import start_game
import pygame
import pygame_menu

"""Initiates pygame"""
pygame.init()

user_name = "Karl XII"
game_difficulty = 3
user_country  = 1
music_volume = 1

def set_music_volume(index, value):
    """Saves music volume in a variable"""
    global music_volume
    music_volume = value
    
    print(f"Music volume set to: {music_volume}")

def save_user_name(value):
    """Saves username in variable"""
    global user_name
    user_name = value
    print(user_name)

def save_user_country(index, value):
    """Save which country is selected in a variable"""
    global user_country
    user_country = value
    if value == 1:
        country = "Sweden"

    elif value == 2:
        country = "Denmark"

    elif value == 3:
        country = "Rome"
    print(f"User country set to: {country}")

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
    start_game.window(game_difficulty, user_country, user_name, music_volume)
    pass

def menu():
    """Menu"""
    surface = pygame.display.set_mode((600, 400))

    menu = pygame_menu.Menu('Imperium Aureum', 600, 400,
    theme=pygame_menu.themes.THEME_BLUE)

    menu.add.text_input('Ruler Name: ', default='Karl XII', onchange=save_user_name)
    menu.add.selector('Country: ', [('Sweden', 1), ('Denmark', 2), ('Rome', 3)], onchange=save_user_country)
    menu.add.selector('Difficulty: ', [('Hard', 3), ('Medium', 2), ('Easy', 1)], onchange=set_difficulty)
    menu.add.selector('Music Volume: ', [('1', 1), ('0.9', 0.9), ('0.8', 0.8), ('0.7', 0.7), ('0.6', 0.6), \
                                        ('0.5', 0.5), ('0.4', 0.4), ('0.2', 0.2), ('0.1', 0.1)], onchange=\
                                        set_music_volume)
    menu.add.button('Play', start_the_game)
    menu.add.button('Quit', pygame_menu.events.EXIT)
    menu.mainloop(surface)
