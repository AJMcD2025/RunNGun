from .weapons import Weapon

class SMG(Weapon):
    def __init__(self):
        super().__init__(
            fire_rate=0.1, # fast firing
            damage=1, # low damage per bullet
            bullet_speed=600 # fast bullets
        )

