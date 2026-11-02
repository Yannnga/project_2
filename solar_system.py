"""
Program: Solar System Explorer - Solar System
Author: Xinyi Yang
Purpose: Create and manage the Sun and eight planets and their orbital movement.
Starter/resources: Python Crash Course
Date: November 2026
"""

import pygame
import json
from pathlib import Path
from celestial_body import CelestialBody

class SolarSystem:
    # A class to manage the celestial bodies.
    def __init__(self, game):
        self.game = game
        self.bodies = pygame.sprite.Group()

        #Planetary orbital radius
        
        mercury_orbit = 55
        venus_orbit = 90
        earth_orbit = 125
        mars_orbit = 160
        jupiter_orbit = 210
        saturn_orbit = 265
        uranus_orbit = 325
        neptune_orbit = 385

        #Planet colors, sizes, and positions
        self.sun = CelestialBody("Sun", (255, 251, 0), 30, 450, 300) #Gold
        self.bodies.add(self.sun)

        self.mercury = CelestialBody("Mercury", (190, 190, 190), 4, 450 + mercury_orbit, 300, 0.005 / 0.241) #Grey
        self.bodies.add(self.mercury)

        self.venus = CelestialBody("Venus", (255, 236, 139), 7, 450 + venus_orbit, 300, 0.012 / 0.615) #light gold
        self.bodies.add(self.venus)

        self.earth = CelestialBody("Earth", (58, 95, 205), 8, 450 + earth_orbit, 300, 0.012 / 1.0) #blue
        self.bodies.add(self.earth)

        self.mars = CelestialBody("Mars", (178, 34, 34), 5, 450 + mars_orbit, 300, 0.012 / 1.881) #red brown
        self.bodies.add(self.mars)

        self.jupiter = CelestialBody("Jupiter", (210, 180, 140), 20, 450 + jupiter_orbit, 300, 0.012 / 11.86) #light brown
        self.bodies.add(self.jupiter)

        self.saturn = CelestialBody("Saturn", (255, 236, 139), 17, 450 + saturn_orbit, 300, 0.012 / 29.46)  #light gold
        self.bodies.add(self.saturn)

        self.uranus = CelestialBody("Uranus", (244, 255, 255), 12, 450 + uranus_orbit, 300, 0.012 / 84.0) # light blue 
        self.bodies.add(self.uranus)

        self.neptune = CelestialBody("Neptune", (170, 216, 230), 11, 450 + neptune_orbit, 300, 0.012 / 164.8) #light bule
        self.bodies.add(self.neptune)

        print("Number of celestial bodies:", len(self.bodies))


    def draw(self):
        #Draw the orbits
        orbital_radius = [55, 90, 125, 160, 210, 265, 325, 385]
        for radius in orbital_radius:
            pygame.draw.ellipse(self.game.screen, (100, 100, 100), (450 - radius, 300 - radius * 0.5, radius * 2, radius), 1)


        #Draw all celestial bodies.
        for body in self.bodies:
            body.draw_body(self.game.screen)

    def update(self):
        #Update all celestial bodies.
        for body in self.bodies:
            body.update()

    def check_body_click(self, mouse_pos):
    # Check if a celestial body was clicked.
        for body in self.bodies:
            if body.rect.collidepoint(mouse_pos):
                print("Selected:", body.name)
                return body
        return None

    
            