import pygame

class Pickup(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()

        # Temporary visual (replace with sprite later)
        self.image = pygame.Surface((20, 20))
        self.image.fill((0, 255, 0))

        self.rect = self.image.get_rect(center=pos)

    def update(self, dt):
        pass

    def on_collect(self, player):
        pass