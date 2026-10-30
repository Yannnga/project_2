import pygame
import math
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from solar_system import SolarSystem

class CelestialBody(Sprite):
    #A class to represent a celestial body.
    def __init__(self, name: str, color: tuple, radius: int, x: int, y: int):
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

        # Set initial position
        self.rect = self.image.get_rect()
        #print("Image after rect creation:", self.image)
        self.rect.center = (x, y)

    def draw_body(self, screen):
        #Draw the celestial body on the screen.
        screen.blit(self.image, self.rect)