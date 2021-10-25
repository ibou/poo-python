from model.player import Player
from model.player import Warrior
from model.weapon import Weapon

knife = Weapon("Couteau", 7)
revolver = Weapon("Pistolet", 6)

player = Player("SAOLA", 20, 2, revolver)

warrior = Warrior("Sangokoun", 20, 7)
warrior.damage(3)
print("vie", warrior.get_health(), "armure", warrior.get_armor_point())
if issubclass(Warrior, Player):
    print("Yes herirtage Ok")
