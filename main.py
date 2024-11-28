import pygame
from constants import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    print("Initializing game")
    num_pass, num_fail = pygame.init()
    
    #todo num_fail is 1, how do I know which module failed to initialize?
    
    # if num_fail > 0:
    #     print(f"num pass : #{num_pass}")
    #     print(f"num fail : #{num_fail}")
    #     raise Exception("Error initializing pygame module!")
    print(f"pygame running : {pygame.get_init()}")


if __name__ == "__main__":
    main()