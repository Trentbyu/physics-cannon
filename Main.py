"""
 Show how to fire bullets at the mouse.
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
"""
from cmath import pi
from ctypes.wintypes import RGB
import pygame
import random
import math

from PIL import Image

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
 
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
# --- Classes
pygame.init()
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
 

# Load image
image = pygame.image.load('target.jpg')
DEFAULT_IMAGE_SIZE = (20, 20)
target = pygame.transform.scale(image, DEFAULT_IMAGE_SIZE)

image = pygame.image.load('cannon ball_1.png')
DEFAULT_IMAGE_SIZE = (10, 10)
cannonball = pygame.transform.scale(image, DEFAULT_IMAGE_SIZE)

image = pygame.image.load('cannon.jpg')
DEFAULT_IMAGE_SIZE = (20, 20)
rifle = pygame.transform.scale(image, DEFAULT_IMAGE_SIZE)



image = pygame.image.load('rod.png')
DEFAULT_IMAGE_SIZE = (50, 100)
rod_pic = pygame.transform.scale(image, DEFAULT_IMAGE_SIZE)

class Block(pygame.sprite.Sprite):
    """ This class represents the block. """
    def __init__(self, image):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        self.image =  image
        
 
        self.rect = self.image.get_rect()
 
 
class Player(pygame.sprite.Sprite):
    """ This class represents the Player. """
 
    def __init__(self):
        """ Set up the player on creation. """
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        self.image = rifle
       
 
        self.rect = pygame.Rect(-500, -200, 20,20)

    def roate(self, start_x, start_y, dest_x, dest_y):
       
        x_diff = dest_x - start_x
        y_diff = dest_y - start_y
        angle = math.atan2(y_diff, x_diff)
        angle  = (angle / (pi)) * 180
        image = pygame.transform.rotate(rifle, - angle)
        self.image = image
        
        
 
class Bullet(pygame.sprite.Sprite):
    """ This class represents the bullet. """
 
    def __init__(self, start_x, start_y, dest_x, dest_y):
        """ Constructor.
        It takes in the starting x and y location.
        It also takes in the destination x and y position.
        """
 
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        # Set up the image for the bullet
        self.image = pygame.Surface([4, 10])
        self.image = cannonball
 
        self.rect = self.image.get_rect()
 
     
        self.rect.x = start_x
        self.rect.y = start_y
 
        # Because rect.x and rect.y are automatically converted
        # to integers, we need to create different variables that
        # store the location as floating point numbers. Integers
        # are not accurate enough for aiming.
        self.floating_point_x = start_x
        self.floating_point_y = start_y
 
        # Calculation the angle in radians between the start points
        # and end points. This is the angle the bullet will travel.
        x_diff = dest_x - start_x
        y_diff = dest_y - start_y
        angle = math.atan2(y_diff, x_diff)
 
        # Taking into account the angle, calculate our change_x
        # and change_y. Velocity is how fast the bullet travels.
        velocity = 5
        self.change_x = math.cos(angle) * velocity 
        self.change_y = math.sin(angle) * velocity 
        
 
    def update(self):
        """ Move the bullet. """
 
        # The floating point x and y hold our more accurate location.
       
      
        if self.rect.x > 0 or self.rect.x < 700 :
            
            self.floating_point_x += self.change_x
            self.rect.x = int(self.floating_point_x)
       
        # If the bullet flies of the screen, get rid of it.
        if self.rect.x < 0 or self.rect.x > 700 :
            
            self.floating_point_x -= self.change_x           
            self.rect.x = int(self.floating_point_x)

        if self.rect.x > 0 or self.rect.y < 500 :
            
            self.floating_point_y += self.change_y            
            self.rect.y = int(self.floating_point_y)
       
        # If the bullet flies of the screen, get rid of it.
        if self.rect.y < 0 or self.rect.y > 500 :
            
            self.floating_point_y -= self.change_y
            self.rect.y= int(self.floating_point_y)
 
         

    
    
 
 

class rod(pygame.sprite.Sprite):
       
       def __init__(self):
        """ Set up the player on creation. """
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        self.image = rod_pic
       
        
        self.rect = pygame.Rect(-500, -200, 20,20)

 
 
# --- Create the window
 
# Initialize Pygame

 
# Set the height and width of the screen
 

 
# --- Sprite lists
 
# This is a list of every sprite. All blocks and the player block as well.
player_group =  pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()
 
# List of each block in the game
block_list = pygame.sprite.Group()
 
# List of each bullet
bullet_list = pygame.sprite.Group()

rod_list = pygame.sprite.Group()
Rod = rod()
rod_list.add(Rod)
# --- Create the sprites
 
for i in range(50):
    # This represents a block
    block = Block( target)
 
    # Set a random location for the block
    block.rect.x = random.randrange(700)
    block.rect.y = random.randrange(SCREEN_HEIGHT - 50)
 
    # Add the block to the list of objects
    block_list.add(block)
    all_sprites_list.add(block)
 
# Create a red player block
player = Player()
player_group.add(player)

 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
score = 0
 
player.rect.x = 0
player.rect.y = SCREEN_HEIGHT - 25
Rod.rect.x = 500
Rod.rect.y = SCREEN_HEIGHT/2
 
# -------- Main Program Loop -----------
while not done:
    pos = pygame.mouse.get_pos()
 
    mouse_x = pos[0]
    mouse_y = pos[1]
 
    # --- Event Processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Fire a bullet if the user clicks the mouse button
 
            # Get the mouse position
            pos = pygame.mouse.get_pos()
 
            mouse_x = pos[0]
            mouse_y = pos[1]
 
            # Create the bullet based on where we are, and where we want to go.
            bullet = Bullet(player.rect.x, player.rect.y, mouse_x, mouse_y)
 
            # Add the bullet to the lists
            all_sprites_list.add(bullet)
            bullet_list.add(bullet)
            
 
    # --- Game logic
 
    # Call the update() method on all the sprites

  
    all_sprites_list.update()
    for players in player_group:
        players.roate(player.rect.x, player.rect.y, mouse_x, mouse_y)
    # Calculate mechanics for each bullet
    for bullet in bullet_list:
 
        # See if it hit a block
        block_hit_list = pygame.sprite.spritecollide(bullet, block_list, True)
 
        # For each block hit, remove the bullet and add to the score
        for block in block_hit_list:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
            score += 1
            print(score)
 
        # Remove the bullet if it flies up off the screen
        
 
    # --- Draw a frame
 
    # Clear the screen
    screen.fill(WHITE)
 
    # Draw all the spites
    all_sprites_list.draw(screen)
    player_group.draw(screen)
    rod_list.draw(screen)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 20 frames per second
    clock.tick(60)
 
pygame.quit()