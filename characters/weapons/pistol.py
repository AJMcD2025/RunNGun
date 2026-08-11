from .weapons import Weapon

class Pistol(Weapon):
    def __init__(self):
        super().__init__(
            fire_rate=0.4, # slower firing
            damage=2, # stronger than SMG
            bullet_speed=500 # medium speed    
        )
        