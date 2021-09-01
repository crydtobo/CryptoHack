import random

class Rocket:
    def __init__(self):
        self.altitude = 0
    def moveUp(self):
        self.altitude += 1

rockets = [Rocket() for _ in range(5)]

print(rockets)
for _ in range(10):
    randomMoveUp = random.randint(0, 4)
    rockets[randomMoveUp].moveUp()


