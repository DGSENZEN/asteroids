#!/usr/bin/env python3
import sys
import pygame
from asteroidfield import AsteroidField
from asteroid import Asteroid
from constants import *
from player import Player
from bullet import Bullet


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    Bullet.containers = (bullets, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    clock = pygame.time.Clock()
    while True:
        for obj in updatable:
            obj.update(dt)
        screen.fill(BLACK)
        for asteroid in asteroids:
            if asteroid.check_collisions(player):
                print("Game Over!")
                sys.exit()
            for bullet in bullets:
                if bullet.check_collisions(asteroid):
                    asteroid.split()
                    bullet.kill()
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
