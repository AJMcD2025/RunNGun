import pygame  # type: ignore

class Enemy:
    def __init__(self, player_pos=None, dt=0):
        self.enemy_pos = pygame.Vector2(100, 100)
        self.player_pos = player_pos or pygame.Vector2(0, 0)
        self.dt = dt

    def update(self):
        # enemy follows player
        direction = self.player_pos - self.enemy_pos
        if direction.length() > 0:
            direction = direction.normalize()
            self.enemy_pos += direction * 150 * self.dt