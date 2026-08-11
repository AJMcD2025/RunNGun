from .player import Player
from ..weapons.smg import SMG
from ..utils.graphics import load_image

class NinjaAlice(Player):
    def __init__(self, pos):
        super().__init__(
            pos, 
            weapon=SMG(), 
            max_health=80,
            move_speed=220,
            jump_height=520
        )

        sheet = load_image("ninja_alice.png")

        self.animations = {
            "idle": [sheet.get_frame(0), sheet.get_frame(1)],
            "run": [sheet.get_frame(2), sheet.get_frame(3), sheet.get_frame(4), sheet.get_frame(5)],
            "jump": [sheet.get_frame(6)]
        }
        
