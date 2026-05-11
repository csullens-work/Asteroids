"""Main entry point for the Asteroids game."""
import pygame
from constants import *
from logger import log_state

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        log_state()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Log the game state (placeholder, replace with actual game state)
        # log_state(screen_size=(SCREEN_WIDTH, SCREEN_HEIGHT))

        screen.fill("black")
        pygame.display.flip()

if __name__ == "__main__":
    main()
