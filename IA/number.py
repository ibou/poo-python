import sys
from random import randint


class Mystere:
    number = ""
    number_to_find = randint(0, 30)
    atempts = 0
    TOP_TRIES = 4

    def choose(self):
        while self.number != self.number_to_find and self.atempts < self.TOP_TRIES:
            self.number = input("Devinez un nombre entre 0 et 30 : ")
            if not self.number.isdigit():
                continue
            self.atempts += 1

            if int(self.number) < self.number_to_find:
                print("choisir un nombre plus grand")
            elif int(self.number) > self.number_to_find:
                print("choisir un nombre plus petit")
            else:
                print("Bravoooo !!!")
                print(f" vous avez trouvé en {self.atempts} tentatives")
                sys.exit()

            print("Il vous rest ", self.TOP_TRIES - self.atempts, "essais")

        print(f"Il fallait choisir le {self.number_to_find}")
        print("Nulllllllllllllllllllll, Good by !!!!!!")
        sys.exit()


if __name__ == '__main__':
    mystere = Mystere()
    mystere.choose()
    print(f"Vous avez choisi {mystere.number} au lieu de {mystere.number_to_find}")
