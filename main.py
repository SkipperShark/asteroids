import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    print("Initializing game")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt_s = 0
    
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables)
    Shot.containers = (updatables, drawables, shots)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill(SCREEN_COLOR)
        
        for sprite in drawables:
            sprite.draw(screen)
        
        dt_ms = clock.tick(MAX_FPS)
        dt_s = dt_ms / 1000
        
        for sprite in updatables:
            sprite.update(dt_s)
            
        for asteroid in asteroids:
            if asteroid.collided(player):
                print("Game over!")
                sys.exit()
            for shot in shots:
                if shot.collided(asteroid):
                    asteroid.split()
                    shot.kill()
                
        for shot in shots:
            shot.update(dt_s)

        pygame.display.flip()

if __name__ == "__main__":
    main()