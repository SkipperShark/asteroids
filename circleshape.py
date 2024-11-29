import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass
    
    def collided(self, other_circle):
        collision_distance = self.radius + other_circle.radius
        distance_to_other_circle = self.position.distance_to(other_circle.position)
        print(f"collision_distance : {collision_distance}")
        print(f"distance_to_other_circle : {distance_to_other_circle}")
        if distance_to_other_circle <= collision_distance:
            return True
        return False
        