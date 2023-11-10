"""Contains game"""
import pygame
import game_init
import world

"""Initialize pygame"""
pygame.init()

"""Set width and height"""
(width, height) = (600, 400)

"""Starting index for music"""
music_index = -1

"""Colors"""
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

objects = []

class Button():
    def __init__(self, x, y, width, height, buttonText='button', onlclickFunction=None, onePress=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onlclickFunction
        self.onePress = onePress
        self.alreadyPressed = False

        self.fillColors = {
            'normal' : red,
            'hover' : '#666666',
            'pressed' : '#333333',
        }

        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.buttonSurf = font_style.render(buttonText, True, (20, 20, 20))

        objects.append(self)

    def process(self):
        mousePos = pygame.mouse.get_pos()
        self.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColors['pressed'])
                if self.onePress:
                    self.onclickFunction()
                elif not self.alreadyPressed:
                    self.onclickFunction()
                    self.alreadyPressed = True

            else:
                self.alreadyPressed = False

        self.buttonSurface.blit(self.buttonSurf, [
        self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2,
        self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2
        ])
        screen.blit(self.buttonSurface, self.buttonRect)

class Cities:
    def __init__(self):
        self.cities = []

    def add_cities(self, city_name):
        if city_name in self.cities:
            self.cities = self.cities
        else:
            self.cities.append(city_name)

    def remove_city(self, city_name):
        if city_name in self.cities:
            self.cities.remove(city_name)

    def get_city_count(self):
        total = 0
        for item in self.cities:
            print(item)
            total += 1
        return total

class Buildings:
    def __init__(self):
        self.buildings = {}

    def add_buildings(self, building_type, count):
        if building_type in self.buildings:
            self.buildings[building_type] += count
        else:
            self.buildings[building_type] = count

    def remove_building(self, building_type, count):
        if building_type in self.buildings:
            self.buildings[building_type] = max(0, self.buildings[building_type] - count)
            if self.buildings[building_type] == 0:
                del self.buildings[building_type]

    def get_building_count(self, building_type):
        return self.buildings.get(building_type, 0)
    
    def get_total_buildings(self):
        total = 0
        for count in self.buildings.values():
            total += count
        print(f"{self.buildings.keys()} : {self.buildings.values()}")
        return total

class Resources:
    def __init__(self):
        self.resources = {}

    def add_resource(self, resource_type, count):
        if resource_type in self.resources:
            self.resources[resource_type] += count
        else:
            self.resources[resource_type] = count

    def remove_resource(self, resource_type, count):
        if resource_type in self.resources:
            self.resources[resource_type] = max(0, self.resources[resource_type] - count)
            if self.resources[resource_type] == 0:
                del self.resources[resource_type]

    def get_resource_count(self, resource_type):
        return self.resources.get(resource_type, 0)

"""Define what a garrison is and how to work with it"""
class Garrison:
    def __init__(self):
        self.units = {}

    def add_unit(self, unit_type, count):
        if unit_type in self.units:
            self.units[unit_type] += count
        else:
            self.units[unit_type] = count

    def remove_unit(self, unit_type, count):
        if unit_type in self.units:
            self.units[unit_type] = max(0, self.units[unit_type] - count)
            if self.units[unit_type] == 0:
                del self.units[unit_type]

    def get_total_units(self):
        total = 0
        for count in self.units.values():
            print(f"{self.units.keys()} : {self.units.values()}")
            total += count
        return total

    def get_unit_count(self, unit_type):
        return self.units.get(unit_type, 0)
    


"""Define screen"""
screen = pygame.display.set_mode((width, height))

"""Define font styles"""
font_style = pygame.font.SysFont("Times New Roman", 25)
font_style_large = pygame.font.SysFont("Times New Roman", 25)

"""Make it possible to draw an image as background"""
class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

def message(msg, color):
    """Make it possible to draw an message on screen"""
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [width / 6, height / 3])

def display_economy(msg):
    """Displays current money"""
    msg = str(msg)

    mesg_larger = font_style_large.render(msg, True, black)

    screen.blit(mesg_larger, [5, 5])

def display_ruler(ruler):
    msg = str(ruler)

    mesg = font_style.render(msg, True, black)
    screen.blit(mesg, [5, 370])

def initial_buildings():
    """Creates the initial buildings for user"""
    global user_buildings

    user_buildings = Buildings()

    if user_buildings.get_total_buildings() < building_capacity:
        user_buildings.add_buildings("Farm", 2)
        user_buildings.add_buildings("Barracks", 1)
        user_buildings.add_buildings("Ore mine", 1)

    print(f"nr of Buildings: {user_buildings.get_total_buildings()}")

def easy():
    """Generates starting resources for easy difficulty"""
    global user_cities
    global user_resources
    global user_buildings
    global food_count
    
    user_garrison1 = Garrison()
    user_resources = Resources()
    user_cities = Cities()


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
    
    user_garrison1 = Garrison()
    user_resources = Resources()
    user_cities = Cities()

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

    user_garrison1 = Garrison()
    user_resources = Resources()
    user_cities = Cities()

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

def check_difficulty(difficulty):
    """Checks what difficulty game is running"""
    gold_count = 0

    if difficulty == 1:
        gold_count = easy()

    elif difficulty == 2:
        gold_count = medium()
    
    elif difficulty == 3:
        gold_count = hard()

    print("Starting resources set")
    return gold_count

def init_user_country(value):
    country = ""

    if value == 1:
        country = "Sweden"
        user_cities.add_cities("Stockholm")
        print(f"Number of cities: {user_cities.get_city_count()}")

    elif value == 2:
        country = "Denmark"
        user_cities.add_cities("Copenhagen")
        print(f"Number of cities: {user_cities.get_city_count()}")
    
    elif value == 3:
        country = "Rome"
        user_cities.add_cities("Rome")
        print(f"Number of cities{user_cities.get_city_count()}")


def music_play(volume):
    """Music player"""
    global music_index

    music_files = ["data/music/IntheHalloftheMountainKing.mp3", "data/music/Carmen_Act_1.mp3"]
    
    music_index += 1

    if music_index >= len(music_files):
        music_index = 0
    
    pygame.mixer.music.load(music_files[music_index])
    pygame.mixer.music.set_volume(volume)
    print(f"Volume set to: {volume}")

    pygame.mixer.music.play()
    print("Music is playing.")
    print("Volume is set to: " + str(pygame.mixer.music.get_volume()))
    print(f"Music is playing ={pygame.mixer.music.get_busy()}")

def window(difficulty, country, ruler, volume):
    """Draws a window"""
    global gold_count
    global user_country
    global building_capacity


    gold_count = check_difficulty(difficulty)
    init_user_country(country)
    
    user_country = game_init.check_user_country(country)

    """maximum buildings is 6 per city"""
    building_capacity = 6 * user_cities.get_city_count()

    initial_buildings()
    music_play(volume)


    resources = str(gold_count) + " Gold | " + str(food_count) + " Food |"

    pygame.display.set_caption('Imperium Aureum')

    BackGround = world.GameBoard()

    Button(495, 325, 100, 40, 'End Turn', game_init.end_turn())

    screen.fill(white)
    screen.blit(BackGround.main(ruler, resources, volume))
    if BackGround is not None:
        screen.blit(BackGround, (0, 0))
    message("Press 'q' to quit", white)
    display_economy(resources)
    display_ruler(ruler)

    pygame.display.flip()

    running = True

    while running:

        music_busy = pygame.mixer.music.get_busy()

        if music_busy == False:
            music_play(volume)
            print("Music restarted")

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.mixer.music.stop()
                        pygame.mixer.music.unload()
                        print(pygame.mixer.music.get_busy())
                        print("q was pressed")
                        running = False

            if event.type == pygame.QUIT:
                running = False
