class Weapon:
    def __init__(self, fire_rate, damage, bullet_speed):
        # time between shots (seconds)
        self.fire_rate = fire_rate
        # damage per bullet
        self.damage = damage
        # pixels per second
        self.bullet_speed = bullet_speed

        # internal cooldown timer
        self.cooldown = 0.0

    def update(self, dt):
        # reduce cooldown over time
        if self.cooldown > 0:
            self.cooldown -= dt

    def can_fire(self):
        return self.cooldown <= 0

    def fire(self, owner_pos, bullets_group):
        # base weapon: single straight bullet
        if not self.can_fire():
            return

        self.cooldown = self.fire_rate

        # you will hook this into your Bullet class later
        # e.g. bullets_group.add(Bullet(owner_pos, self.bullet_speed, self.damage))