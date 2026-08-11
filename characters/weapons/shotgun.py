from .weapons import Weapon
from bullets.bullets import Bullet

class Shotgun(Weapon):
    def __init__(self):
        super().__init__(
            fire_rate=0.8,  # slow firing
            damage=1,  # per pellet
            bullet_speed=450  # slower bullets
        )

    def fire(self, owner_pos, direction,bullets_group):
        if not self.can_fire():
            return

        self.cooldown = self.fire_rate

        # Shotgun fires 5 pellets with slight angle differences
        angles = [-10, -5, 0, 5, 10]

        for angle in angles:
            bullet = Bullet(
                pos=owner_pos,
                direction=direction,
                speed=self.bullet_speed,
                damage=self.damage
            )
            bullets_group.add(bullet)