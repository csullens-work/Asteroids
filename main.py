"""Main entry point for the Asteroids game."""
import pygame
from constants import *
from logger import log_state
from player import Player

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()

    clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Log the game state (placeholder, replace with actual game state)
        # log_state(screen_size=(SCREEN_WIDTH, SCREEN_HEIGHT))

        screen.fill("black")
        player.draw(screen)
        
        pygame.display.flip()

        dt = clock.tick(60) / 1000  # Limit to 60 FPS and get delta time in seconds
        # print(f"Delta time for this frame: {dt:.4f} seconds")

if __name__ == "__main__":
    main()
