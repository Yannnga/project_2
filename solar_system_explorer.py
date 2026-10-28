import pygame
from settings import Settings

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

    def run_game(self):
        while self.running:
            self._check_events()
            self._update_screen()
            self.clock.tick(self.settings.FPS)

        pygame.quit()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def _update_screen(self):
        self.screen.blit(self.bg_image, (0, 0))
        pygame.display.flip()


if __name__ == "__main__":
    game = SolarSystemExplorer()
    game.run_game()