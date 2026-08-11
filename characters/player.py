import pygame  # type: ignore[import-not-found]

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, weapon, bullets_group, pickups_group):
        super().__init__()

        # TEMP sprite (replace with your character sprite later)
        self.image = pygame.Surface((32, 48))
        self.image.fill((0, 0, 255))

        self.rect = self.image.get_rect(topleft=pos)

        # Movement
        self.vel = pygame.Vector2(0, 0)
        self.speed = 200
        self.gravity = 900

        # Facing direction (1 = right, -1 = left)
        self.facing = 1

        # Health
        self.max_health = 100
        self.health = 100

        # Weapon + bullets
        self.weapon = weapon
        self.bullets_group = bullets_group

        # Pickups
        self.pickups_group = pickups_group

    def apply_gravity(self, dt):
        self.vel.y += self.gravity * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        # Movement
        self.vel.x = 0
        if keys[pygame.K_a]:
            self.vel.x = -self.speed
            self.facing = -1
        if keys[pygame.K_d]:
            self.vel.x = self.speed
            self.facing = 1

        # Shooting
        if keys[pygame.K_SPACE]:
            self.weapon.fire(self.rect.center, self.facing, self.bullets_group)

        # Apply movement
        self.apply_gravity(dt)
        self.rect.x += self.vel.x * dt
        self.rect.y += self.vel.y * dt

        # Pickups
        hits = pygame.sprite.spritecollide(self, self.pickups_group, False)
        for pickup in hits:
            pickup.on_collect(self)