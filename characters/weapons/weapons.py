from bullets.bullets import Bullet

class Weapon:
    def __init__(self, fire_rate, damage, bullet_speed):
        self.fire_rate = fire_rate
        self.damage = damage
        self.bullet_speed = bullet_speed
        self.cooldown = 0.0

    def update(self, dt):
        if self.cooldown > 0:
            self.cooldown -= dt

    def can_fire(self):
        return self.cooldown <= 0

    def fire(self, owner_pos, direction, bullets_group):
        if not self.can_fire():
            return

        self.cooldown = self.fire_rate

        bullet = Bullet(
            pos=owner_pos,
            direction=direction,
            speed=self.bullet_speed,
            damage=self.damage
        )

        bullets_group.add(bullet)
        # you will hook this into your Bullet class later
        # e.g. bullets_group.add(Bullet(owner_pos, self.bullet_speed, self.damage))