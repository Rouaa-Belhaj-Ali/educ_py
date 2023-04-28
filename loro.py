import pygame
import random

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Initialize Pygame
pygame.init()

# Set screen size
size = (700, 500)
screen = pygame.display.set_mode(size)

# Set window title
pygame.display.set_caption("Alien Game")

# Set font for displaying score
font = pygame.font.SysFont('Calibri', 25, True, False)

# Set initial score to 0
score = 0

# Define alien image
alien_img = pygame.image.load('images/lili.png')

# Set initial alien position
alien_x = random.randint(0, size[0])
alien_y = -100

# Set speed of alien
alien_speed = 5

# Set game loop condition
done = False

# Main game loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    # Fill screen with white
    screen.fill(WHITE)
    
    # Move alien down the screen
    alien_y += alien_speed
    
    # Draw alien on screen
    screen.blit(alien_img, (alien_x, alien_y))
    
    # Display score on screen
    text = font.render("Score: " + str(score), True, BLACK)
    screen.blit(text, [10, 10])
    
    # Update screen
    pygame.display.update()
    
    # Check if alien has reached the bottom of the screen
    if alien_y > size[1]:
        # If so, reset alien position
        alien_x = random.randint(0, size[0])
        alien_y = -100
        # Increase score by 1
        score += 1

# Quit Pygame
pygame.quit()




