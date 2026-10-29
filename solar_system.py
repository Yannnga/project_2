import pygame
from celestial_body import CelestialBody

class SolarSystem:
    # A class to manage the celestial bodies.
    def __init__(self, game):
        self.game = game
        self.bodies = pygame.sprite.Group()

        self.earth = CelestialBody("Earth", (70, 130, 255), 8)

        self.bodies.add(self.earth)

    def draw(self):
        #Draw all celestial bodies.
        for body in self.bodies:
            body.draw_body(self.game.screen)
            