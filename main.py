"""Main entry point for the Asteroids game."""
import sys
import pygame
from constants import *
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()

    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable,
                         drawable)

    Asteroid.containers = (asteroids,
                           updatable,
                           drawable)

    AsteroidField.containers = (updatable)

    Shot.containers = (shots,
                        updatable,
                        drawable)


    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    asteroid_field = AsteroidField()



    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Log the game state (placeholder, replace with actual game state)
        # log_state(screen_size=(SCREEN_WIDTH, SCREEN_HEIGHT))

        screen.fill("black")
        updatable.update(dt)
        asteroids.update(dt)

        for d in drawable:
            d.draw(screen)

        for a in asteroids:
            if player.collides_with(a):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        pygame.display.flip()

        dt = clock.tick(60) / 1000  # Limit to 60 FPS and get delta time in seconds
        # print(f"Delta time for this frame: {dt:.4f} seconds")

if __name__ == "__main__":
    main()
