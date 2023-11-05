"""Contains game"""
import pygame

"""Initialize pygame"""
pygame.init()

"""Set width and height"""
(width, height) = (600, 400)

"""Colors"""
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

"""Define what a garrison is"""
class Garrison:
    def __init__(self):
        self.units = {}  # A dictionary to store unit types and their counts

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
            total += count
        return total

    def get_unit_count(self, unit_type):
        return self.units.get(unit_type, 0)
    


"""Define screen"""
screen = pygame.display.set_mode((width, height))

"""Define font styles"""
font_style = pygame.font.SysFont("bahnschrift", 25)

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
    msg = str(msg) + " Gold"

    mesg = font_style.render(msg, True, black)
    screen.blit(mesg, [5, 0])

def easy():
    money = 1200
    user_garrison1 = Garrison()
    user_garrison1.add_unit("Musketmen", 120)
    user_garrison1.add_unit("Musketmen", 120)
    user_garrison1.add_unit("Musketmen", 120)
    user_garrison1.add_unit("Musketmen", 120)
    user_garrison1.add_unit("Musketmen", 120)
    user_garrison1.add_unit("Musketmen", 120)
    user_garrison1.add_unit("Musketmen", 120)
    user_garrison1.add_unit("Spearmen", 200)
    user_garrison1.add_unit("Spearmen", 200)
    user_garrison1.add_unit("Spearmen", 200)

    total_units = user_garrison1.get_total_units()
    musketmen_count = user_garrison1.get_unit_count("Musketmen")
    spear_men_count = user_garrison1.get_unit_count("Spearmen")
    
    print(f"Spearmen count: {spear_men_count}")
    print(f"Musketmen count: {musketmen_count}")
    print(f"Total units in the garrison: {total_units}")
    
    return money

def medium():
    money = 800
    user_garrison1 = Garrison()
    user_garrison1.add_unit("Musketmen", 120)
    user_garrison1.add_unit("Musketmen", 120)
    user_garrison1.add_unit("Musketmen", 120)
    user_garrison1.add_unit("Musketmen", 120)
    
    total_units = user_garrison1.get_total_units()
    musketmen_count = user_garrison1.get_unit_count("Musketmen")
    spear_men_count = user_garrison1.get_unit_count("Spearmen")

    print(f"Spearmen count: {spear_men_count}")
    print(f"Musketmen count: {musketmen_count}")
    print(f"Total units in the garrison: {total_units}")

    return money

def hard():
    money = 400
    user_garrison1 = Garrison()
    user_garrison1.add_unit("Musketmen", 120)
    user_garrison1.add_unit("Musketmen", 120)
    user_garrison1.add_unit("Musketmen", 120)
    user_garrison1.add_unit("Musketmen", 120)

    total_units = user_garrison1.get_total_units()
    musketmen_count = user_garrison1.get_unit_count("Musketmen")
    spear_men_count = user_garrison1.get_unit_count("Spearmen")

    print(f"Spearmen count: {spear_men_count}")
    print(f"Musketmen count: {musketmen_count}")
    print(f"Total units in the garrison: {total_units}")

    return money

def check_difficulty(difficulty):
    """Checks what difficulty game is running"""
    money = 0

    if difficulty == 1:
        money = easy()

    elif difficulty == 2:
        money = medium()
    
    elif difficulty == 3:
        money = hard()

    print("Starting resources set")
    return (money)

def check_user_country(value):
    country = ""

    if value == 1:
        country = "Sweden"

    elif value == 2:
        country = "Denmark"
    
    elif value == 3:
        country = "Rome"

    return country

def window(difficulty, country):
    """Draws a window"""
    global money
    money = check_difficulty(difficulty)
    user_country = check_user_country(country)

    pygame.display.set_caption('Imperium Aureum')

    BackGround = Background('data/pictures/karlxii.jpg', [0,0])

    screen.fill([255, 255, 255])
    screen.blit(BackGround.image, BackGround.rect)
    message("Press 'q' to quit", white)
    display_economy(money)

    pygame.display.flip()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        print("q was pressed")
                        running = False

            if event.type == pygame.QUIT:
                running = False
