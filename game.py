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

def check_difficulty(difficulty):
    """Checks what difficulty game is running"""
    money = 0

    if difficulty == 1:
        money = 1200

    elif difficulty == 2:
        money = 800
    
    elif difficulty == 3:
        money = 400

    return money


def window(difficulty):
    """Draws a window"""
    global money
    money = check_difficulty(difficulty)

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
