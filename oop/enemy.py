""" Each enemy has 10 health points and 1 attack_damage, but what we don't know the type of enemy"""

# What kind of state data do you want to track


class Enemy:
    def __init__(self, type_of_enemy, health_points=10, attack_damage=1):
        self.__type_of_enemy = type_of_enemy
        self.health_points = health_points
        self.attack_damage = attack_damage

    @property
    def get_type_of_enemy(self):
        return self.__type_of_enemy

    def talk(self):
        print(f"I am {self.__type_of_enemy}, be prepared to fight!")

    def walk_forward(self):
        print(f"{self.__type_of_enemy} moves closer")

    def attack(self):
        print(f"{self.__type_of_enemy} attacks for {self.attack_damage} damage")

    def special_attack(self):
        print("special attack")


enemy = Enemy("Zombie")

print(enemy.health_points)
print(enemy.get_type_of_enemy)
enemy.talk()
enemy.walk_forward()
enemy.attack()
