class Player:

    def __init__(self, pseudo, health, attack, weapon=None):
        self.pseudo = pseudo
        self.health = health
        self.attack = attack
        self.weapon = weapon
        print("Bienvenu au joueur ", self.pseudo, "/ Health ", self.health, " / Attack ", self.attack, " / Arme")

    def get_pseudo(self):
        return self.pseudo

    def get_health(self):
        return self.health

    def get_attack_value(self):
        return self.attack

    def damage(self, damage):
        self.health -= damage

    def attack_player(self, target_player):
        target_player.damage(self.weapon.damage)


class Warrior(Player):

    def __init__(self, pseudo, health, attack, armor=3):
        super().__init__(pseudo, health, attack)
        self.armor = armor
        print("Bienvenu au Guerrier ", self.pseudo, "/ Health ", self.health, " / Attack ", self.attack, " / Arme")

    def damage(self, damage):
        if self.armor > 0:
            self.armor -= 1
            damage = 0
        super().damage(damage)

    def attack_player(self, target_player):
        target_player.damage(self.attack)

    def blade(self):
        self.armor = 3
        print("Les points d'armure ont été rechargés")

    def get_armor_point(self):
        return self.armor
