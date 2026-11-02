"""
Program: Solar System Explorer - Celestial Body
Author: Xinyi Yang
Purpose: Define celestial bodies and their orbital movement in the Solar System.
Starter/resources: Python Crash Course, Pygame documentation
Date: November 2026
"""

import pygame
import math
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from solar_system import SolarSystem

class CelestialBody(Sprite):
    #A class to represent a celestial body.
    def __init__(self, name: str, color: tuple, radius: int, x: int, y: int, orbit_speed: float = 0):
        super().__init__()
        self.name = name
        self.color = color
        self.radius = radius

        # Create the celestial body image
        self.image = pygame.Surface(
            (self.radius * 2, self.radius * 2),
            pygame.SRCALPHA
        )
        #print("Image after creation:", self.image)

        pygame.draw.circle(
            self.image,
            self.color,
            (self.radius, self.radius),
            self.radius
        )

        #Set initial position
        self.rect = self.image.get_rect()
        #print("Image after rect creation:", self.image)
        self.rect.center = (x, y)
        self.orbit_radius = x - 450
        self.angle = 0
        self.orbit_speed = orbit_speed

    def draw_body(self, screen):
        #Draw the celestial body on the screen.
        screen.blit(self.image, self.rect)

    def update(self):
        #Update the position of the celestial body
        if self.orbit_radius > 0:
            self.angle += self.orbit_speed

            x = 450 + self.orbit_radius * math.cos(self.angle)
            y = 300 + self.orbit_radius * 0.5 * math.sin(self.angle)

            self.rect.center = (round(x), round(y))