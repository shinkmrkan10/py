# Import the pygame module
import pygame
 
# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
   K_UP,
   K_DOWN,
   K_LEFT,
   K_RIGHT,
   K_ESCAPE,
   KEYDOWN,
   QUIT,
)

# Initialize pygame
pygame.init()

# Define a Player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((50, 25))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect()

# Define constants for the screen width and height
SCREEN_WIDTH = 648
SCREEN_HEIGHT = 486

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
player = Player()
# Variable to keep the main loop running
running = True

# Main loop
while running:
    # Fill the screen with black
    screen.fill((0, 0, 0))
    bg = pygame.image.load("hello/jra.jpg")
    rect_bg = bg.get_rect()
    screen.blit(bg, rect_bg)

    # Draw the player on the screen
    screen.blit(player.surf, player.rect)

    # Update the display
    pygame.display.flip()   # Look at every event in the queue
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False

        # Did the user click the window close button? If so, stop the loop.
        elif event.type == QUIT:
            running = False



