import pygame
import start_game
from start_game import *

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

def easy():
    """Generates starting resources for easy difficulty"""
    global user_cities
    global user_resources
    global user_buildings
    global food_count
    
    user_garrison1 = start_game.Garrison()
    user_resources = start_game.Resources()
    user_cities = start_game.Cities()

    user_garrison1.add_unit("Musketmen", 840)
    user_garrison1.add_unit("Spearmen", 600)

    user_resources.add_resource("Food", 1000)
    user_resources.add_resource("Gold", 1200)

    total_units = user_garrison1.get_total_units()
    musketmen_count = user_garrison1.get_unit_count("Musketmen")
    spear_men_count = user_garrison1.get_unit_count("Spearmen")

    food_count = user_resources.get_resource_count("Food")
    gold_count = user_resources.get_resource_count("Gold")
    
    print(f"User food: {food_count}")
    print(f"User garrison nr. 1: {user_garrison1}")
    print(f"Spearmen count: {spear_men_count}")
    print(f"Musketmen count: {musketmen_count}")
    print(f"Total units in the garrison: {total_units}")
    
    return gold_count

def medium():
    """Generates starting resources for medium difficulty"""
    global user_cities
    global user_resources
    global user_cities
    global food_count
    
    user_garrison1 = start_game.Garrison()
    user_resources = start_game.Resources()
    user_cities = start_game.Cities()

    user_garrison1.add_unit("Musketmen", 480)

    user_resources.add_resource("Food", 1000)
    user_resources.add_resource("Gold", 800)
    
    total_units = user_garrison1.get_total_units()
    musketmen_count = user_garrison1.get_unit_count("Musketmen")
    spear_men_count = user_garrison1.get_unit_count("Spearmen")

    food_count = user_resources.get_resource_count("Food")
    gold_count = user_resources.get_resource_count("Gold")
    
    print(f"User food: {food_count}")
    print(f"User garrison nr. 1: {user_garrison1}")
    print(f"Spearmen count: {spear_men_count}")
    print(f"Musketmen count: {musketmen_count}")
    print(f"Total units in the garrison: {total_units}")

    return gold_count

def hard():
    """Generates starting resources for hard difficulty"""
    global user_cities
    global user_resources
    global user_cities
    global food_count
    global user_garrison1

    user_garrison1 = start_game.Garrison()
    user_resources = start_game.Resources()
    user_cities = start_game.Cities()

    user_garrison1.add_unit("Musketmen", 480)

    user_resources.add_resource("Food", 1000)
    user_resources.add_resource("Gold", 400)

    total_units = user_garrison1.get_total_units()
    musketmen_count = user_garrison1.get_unit_count("Musketmen")
    spear_men_count = user_garrison1.get_unit_count("Spearmen")

    food_count = user_resources.get_resource_count("Food")
    gold_count = user_resources.get_resource_count("Gold")
    
    print(f"User food: {food_count}")
    print(f"User garrison nr. 1: {user_garrison1}")
    print(f"Spearmen count: {spear_men_count}")
    print(f"Musketmen count: {musketmen_count}")
    print(f"Total units in the garrison: {total_units}")

    return gold_count

def ruler_picture(country):
    print(user_garrison1.get_total_units())
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

def end_turn_cost():
    nr_of_cities = user_cities.get_city_count()
    food_count = user_resources.get_resource_count("food")
    gold_count = user_resources.get_resource_count("gold")
    musketmen_count = user_garrison1.get_unit_count("musketmen")
    spearmen_count = user_garrison1.get_unit_count("spearmen")

    print(f"nr of cities: {nr_of_cities}\nfood count: {food_count}\ngold_count: \
        {gold_count}\nmusketmen count: {musketmen_count}\nspearmen count:\
            {spearmen_count}")


def end_turn():
    def click_action():
        print("Turn ended")
        

    return end_turn_cost
