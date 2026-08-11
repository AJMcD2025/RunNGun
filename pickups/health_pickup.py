import pygame
from .pickups import Pickup

class HealthPickup(Pickup):
    def __init__(self, pos, amount=20):
        super().__init__(pos)
        self.amount = amount

        # Different colour so you can see it
        self.image.fill((255, 0, 0))

    def on_collect(self, player):
        player.health = min(player.max_health, player.health + self.amount)
        self.kill()