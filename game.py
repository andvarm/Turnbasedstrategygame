"""Contains game"""
import pygame

# Initialize pygame
pygame.init()

# Set width and height
(width, height) = (600, 400)

# Colors
white = (255, 255, 255)

# Define screen
screen = pygame.display.set_mode((width, height))

# Define font styles
font_style = pygame.font.SysFont("bahnschrift", 25)

# Make it possible to draw an image as background
class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

# Make it possible to draw an message on screen
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [width / 6, height / 3])


# Define window
def window():
    """Draws a window"""
    pygame.display.set_caption('Imperium Aureum')

    BackGround = Background('data/pictures/karlxii.jpg', [0,0])

    screen.fill([255, 255, 255])
    screen.blit(BackGround.image, BackGround.rect)
    message("Press 'q' to quit", white)

    pygame.display.flip()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        print("goodbye")
                        running = False

            if event.type == pygame.QUIT:
                running = False
