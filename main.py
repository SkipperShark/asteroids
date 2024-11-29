import pygame
from constants import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    print("Initializing game")
    pygame.init()
    surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt_s = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        surface.fill(SCREEN_COLOR)
        pygame.display.flip()
        
        dt_ms = clock.tick(MAX_FPS)
        dt_s = dt_ms / 1000

if __name__ == "__main__":
    main()