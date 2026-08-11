import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos, direction, speed, damage):
        super().__init__()

        # Basic visual (replace with your sprite later)
        self,image = pygame.Surface((6, 2))
        self.image.fill((255, 255, 0))

        self.rect = self.image.get_rect(center=pos)

        # Movement
        self.direction = direction # usually 1 or -1
        self.speed = speed

        # damage to apply on hit
        self.damage = damage

    def update(self, dt, level_rects):
        # Move bullets
        self.rect.x += self.direction * self.speed * dt

        # Remove it off-screen
        if self.rect.right < 0 or self.rect.left > 1920:
            self.kill()

        # Collision with level tiles
        for tile in level_rects:
            if self.rect.colliderect(tile):
                self.kill()
                break