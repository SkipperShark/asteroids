from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED
import pygame

class Player(CircleShape):
    LINE_WIDTH = 2
    
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
        
        
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), self.LINE_WIDTH)
        
        
    def rotate(self, dt_s):
        self.rotation += PLAYER_TURN_SPEED * dt_s
        
        
    def update(self, dt_s):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_a]:
            self.rotate(-dt_s)
        if keys[pygame.K_d]:
            self.rotate(dt_s)
        if keys[pygame.K_w]:
            self.move(dt_s)
        if keys[pygame.K_s]:
            self.move(-dt_s)
            
            
    def move(self, dt_s):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt_s
        