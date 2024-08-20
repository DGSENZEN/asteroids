import pygame
from circleshape import *
from constants import ASTEROID_MIN_RADIUS
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)
        a_1 = self.velocity.rotate(random_angle)
        a_2 = self.velocity.rotate(-random_angle)
        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid1.velocity = a_1 * 1.2
        new_asteroid2.velocity = a_2 * 1.2

    def check_collisions(self, other):
        return self.position.distance_to(other.position) <= self.radius + other.radius
