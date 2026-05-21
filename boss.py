class Vector2:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __mul__(self, scalar):
        return Vector2(self.x * scalar, self.y * scalar)

    __rmul__ = __mul__

    def length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def normalize(self):
        length = self.length()
        if length == 0:
            return Vector2(0, 0)
        return Vector2(self.x / length, self.y / length)


class Boss:
    def __init__(self):
        self.boss_pos = Vector2(1000, 500)
        self.player_pos = Vector2(0, 0)
        self.dt = 0.016

    def update(self):
        direction = self.player_pos - self.boss_pos
        if direction.length() > 0:
            direction = direction.normalize()
            self.boss_pos += direction * 80 * self.dt