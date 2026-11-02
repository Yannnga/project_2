"""
Program: Solar System Explorer - Settings
Author: Xinyi Yang
Purpose: Store the settings for the Solar System Explorer, including screen size, FPS, and background.
Starter/resources: Python Crash Course
Date: November 2026
"""

import pygame
import json
from pathlib import Path
from settings import Settings
#from celestial_body import CelestialBody
from solar_system import SolarSystem

class SolarSystemExplorer:

    def __init__(self):
        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_w, self.settings.screen_h)
        )

        pygame.display.set_caption(self.settings.name)

        # Load background image
        self.bg_image = pygame.image.load(self.settings.bg_file).convert()
        self.bg_image = pygame.transform.scale(
            self.bg_image,
            (self.settings.screen_w, self.settings.screen_h)
        )

        self.clock = pygame.time.Clock()
        self.running = True

        self.solar_system = SolarSystem(self)
        self.selected_body = None
        self.font = pygame.font.Font(None, 32)
        data_file = Path(__file__).parent / "data" / "planets.json"
        
        #JSON Exception Handling
        try:
            with open(data_file, "r") as f:
                self.planet_data = json.load(f)
        except (OSError, json.JSONDecodeError) as e:
            print("Error loading planetary data:", e)
            self.planet_data = {}


    def run_game(self):
        while self.running:
            self._check_events()
            self.solar_system.update()
            self._update_screen()
            self.clock.tick(self.settings.FPS)

        pygame.quit()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._check_mouse_events(event)

    def _check_mouse_events(self, event):
        if event.button == 1:
            self.selected_body = self.solar_system.check_body_click(event.pos)

    def _draw_body_info(self):
        if self.selected_body:
            name = self.selected_body.name

            if name in self.planet_data:
                data = self.planet_data[name]
                radius = data["radius_km"]
                period = data["orbital_period"]

                info_text = f"Name: {name}, Radius: {radius} km, Orbital Period: {period} years"
            else:
                info_text = f"Name: {name}"

            text_surface = self.font.render(info_text, True, (255, 255, 255))
            self.screen.blit(text_surface, (10, 10))

    def _update_screen(self):
        self.screen.blit(self.bg_image, (0, 0))
        #self.earth.draw_body(self.screen)
        self.solar_system.draw()
        self._draw_body_info()

        
        pygame.display.flip()


if __name__ == "__main__":
    game = SolarSystemExplorer()
    game.run_game()