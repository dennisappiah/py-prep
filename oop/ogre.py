from enemy import Enemy
import random


# Ogre is-a Enemy
class Ogre(Enemy):
    def __init__(self, health_points, attack_damage):
        super().__init__(
            type_of_enemy="Ogre",
            health_points=health_points,
            attack_damage=attack_damage,
        )

    #   overriding talk method
    def talk(self):
        print("Ogre is slamming hands all around!")

    def special_attack(self):
        did_special_attack_work = random.random() < 0.20
        if did_special_attack_work:
            self.health_points += 4
            print("Ogre regenerated ")


ogre = Ogre(150, 15)
ogre.talk()
