import pygame
import random
import os

# Initialize Pygame
pygame.init()

# Set the dimensions of the game window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Memory Match Game")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_DIR = os.path.join(BASE_DIR, "images")
IMAGE_PATH = os.path.join(IMAGE_DIR, "image.jpg")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Load images
image1 = pygame.image.load("images/image1.jpg")
image2 = pygame.image.load("images/image2.jpg")
image3 = pygame.image.load("images/image3.jpg")
image4 = pygame.image.load("images/image4.jpg")

# Create a list of card images
card_images = [image1, image1, image2, image2, image3, image3, image4, image4]

# Shuffle the card images
random.shuffle(card_images)

# Define the size of the cards and the gap between them
CARD_WIDTH = 150
CARD_HEIGHT = 150
GAP_SIZE = 20

# Define the coordinates of the top left corner of the cards
X_MARGIN = (WINDOW_WIDTH - (4 * CARD_WIDTH + 3 * GAP_SIZE)) // 2
Y_MARGIN = (WINDOW_HEIGHT - (2 * CARD_HEIGHT + GAP_SIZE)) // 2

# Create a list of Rect objects for the card positions
card_rects = []
for i in range(4):
    for j in range(2):
        card_rects.append(pygame.Rect(X_MARGIN + i * (CARD_WIDTH + GAP_SIZE),
                                      Y_MARGIN + j * (CARD_HEIGHT + GAP_SIZE),
                                      CARD_WIDTH, CARD_HEIGHT))

# Create a list of flipped cards
flipped = []

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Draw the game board
    game_window.fill(WHITE)
    for i, rect in enumerate(card_rects):
        if i in flipped:
            # Draw the card image if it is flipped
            game_window.blit(card_images[i], rect)
        else:
            # Draw the card back if it is not flipped
            pygame.draw.rect(game_window, WHITE, rect)
    pygame.display.flip()

    # Check if two cards are flipped
    if len(flipped) == 2:
        # Check if the two flipped cards match
        if card_images[flipped[0]] == card_images[flipped[1]]:
            # Remove the cards from the flipped list if they match
            flipped = []
        else:
            # Flip the cards back if they do not match
            pygame.time.wait(1000)
            flipped = []

    # Check for mouse clicks
    mouse_pos = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONUP:
        for i, rect in enumerate(card_rects):
            if rect.collidepoint(mouse_pos) and i not in flipped:
                flipped.append(i)
                break
