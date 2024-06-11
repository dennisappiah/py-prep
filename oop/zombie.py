from enemy import Enemy


# zombie is-a Enemy
class Zombie(Enemy):
    def __init__(self, health_points, attack_damage):
        super().__init__(
            type_of_enemy="Zombie",
            health_points=health_points,
            attack_damage=attack_damage,
        )

    #   overriding talk method
    def talk(self):
        print("**Grumbling")

    def spread_disease(self):
        print("The zombie is trying to spread disease")


zombie = Zombie(100, 10)
zombie.talk()
zombie.spread_disease()
