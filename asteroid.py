import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
        
    
    def update(self, dt_s):
        self.position += self.velocity * dt_s
        
        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        angle_offset = random.uniform(20, 50)
        child_vector_1 = self.velocity.rotate(angle_offset)
        child_vector_2 = self.velocity.rotate(-angle_offset)
        child_radius = self.radius - ASTEROID_MIN_RADIUS
        child_1 = Asteroid(self.position.x, self.position.y, child_radius)
        child_2 = Asteroid(self.position.x, self.position.y, child_radius)
        child_1.velocity = child_vector_1 * 1.2
        child_2.velocity = child_vector_2
        