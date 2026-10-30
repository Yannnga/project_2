import pygame
from celestial_body import CelestialBody

class SolarSystem:
    # A class to manage the celestial bodies.
    def __init__(self, game):
        self.game = game
        self.bodies = pygame.sprite.Group()

        self.sun = CelestialBody("Sun", (255, 251, 0), 30, 450, 300) #Gold
        self.bodies.add(self.sun)

        '''self.mercury = CelestialBody("Mercury", (190, 190, 190), 4) #Grey
        self.bodies.add(self.mercury)

        self.venus = CelestialBody("Venus", (255, 236, 139), 7 ) #light gold
        self.bodies.add(self.venus)

        self.earth = CelestialBody("Earth", (58, 95, 205), 8) #blue
        self.bodies.add(self.earth)

        self.mars = CelestialBody("Mars", (178, 34, 34), 5) #red brown
        self.bodies.add(self.mars)

        self.jupiter = CelestialBody("Jupiter", (210, 180, 140), 20) #light brown
        self.bodies.add(self.jupiter)

        self.saturn = CelestialBody("Saturn", (255, 236, 139), 17)  #light gold
        self.bodies.add(self.saturn)

        self.uranus = CelestialBody("Uranus", (244, 255, 255), 12) # light blue 
        self.bodies.add(self.uranus)

        self.neptune = CelestialBody("Neptune", (170, 216, 230), 11) #light bule
        self.bodies.add(self.neptune)'''

        print("Number of celestial bodies:", len(self.bodies))


    def draw(self):
        #Draw all celestial bodies.
        for body in self.bodies:
            body.draw_body(self.game.screen)

    
            