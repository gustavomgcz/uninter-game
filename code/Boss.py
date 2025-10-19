import random
from code.Const import ENTITY_SHOOT_DELAY, ENTITY_SPEED, WIN_HEIGHT
from code.BossShoot import BossShoot
from code.Entity import Entity


class Boss(Entity):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.shoot_delay = ENTITY_SHOOT_DELAY[self.name]

    def move(self, ):
        self.rect.centerx -= ENTITY_SPEED[self.name]

    def shoot(self, ):
        self.shoot_delay -= 1
        if self.shoot_delay == 0:
            self.shoot_delay = ENTITY_SHOOT_DELAY[self.name]
            return BossShoot(name=f'{self.name}Shoot', position=(
                self.rect.centerx, random.randint(70, WIN_HEIGHT-75)))

    def is_dead(self):
        return self.is_dead
