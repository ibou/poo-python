import sys


class Choice:
    LIST = []

    MENU = """Choisissez parmi les 5 options
    1: Ajouter un elem
    2: Retirer elem
    3: Afficher list
    4: Vider list
    5: Quit
    """

    MENU_CHOICES = ["1", "2", "3", "4", "5"]

    def choose(self):
        while True:
            user_choice = ""
            while user_choice not in self.MENU_CHOICES:
                user_choice = input(self.MENU)
                if user_choice not in self.MENU_CHOICES:
                    print("bad choice")
            print("===> Votre choix ", user_choice)
            if user_choice == "1":
                item = input("Entre le nom de l'elem : ")
                self.LIST.append(item)
                print(f"L'élément {item} a bien été ajouté")
            elif user_choice == "2":
                item = input("Entre le nom de l'elem a retirer: ")
                if item in self.LIST:
                    self.LIST.remove(item)
                    print(f"L'élément {item} a bien été retiré ")
            elif user_choice == "3":
                print(self.LIST, len(self.LIST))
            elif user_choice == "4":
                self.LIST.clear()
            elif user_choice == "5":
                print("A bientôt")
                sys.exit()
            print("-" * 50)


if __name__ == '__main__':
    choice = Choice()
    print("Start", choice.choose())
