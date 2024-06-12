from zombie import Zombie
from ogre import Ogre
from enemy import Enemy


# Polymorphism
def battle(e1: Enemy, e2: Enemy):
    e1.talk()
    e2.talk()

    while e1.health_points > 0 and e2.health_points > 0:
        print("---------------------")
        e1.special_attack()
        e2.special_attack()
        print(f"{e1.get_type_of_enemy} : {e1.health_points} HP")
        print(f"{e2.get_type_of_enemy} : {e2.health_points} HP")
        e2.attack()
        e1.health_points -= e2.attack_damage


zombie = Zombie(100, 10)
ogre = Ogre(150, 15)

battle(zombie)
battle(ogre)
