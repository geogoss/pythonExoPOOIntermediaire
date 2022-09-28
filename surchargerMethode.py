'''
Surcharger une méthode
Dans cet exercice, vous devez implémenter la méthode parle pour les classes Animal, Chien et Chat.

Dans le cas de la classe Animal, la méthode parle, doit lever une erreur de type NotImplementedError avec le
message d'erreur "Je ne sais pas quoi dire...".

Dans le cas de la classe Chien, vous devez surcharger la méthode parle pour qu'elle retourne la chaîne de
caractères "Woof!".

Pour la classe Chat, la méthode parle doit retourner la chaîne de caractères "Miaou!".
'''

class Animal:
    def __init__(self, nom):
        self.nom = nom

    def parle(self):
        raise NotImplementedError("Je ne sais pas quoi dire...")


class Chien(Animal):
    def __init__(self, nom):
        super().__init__(nom)

    def parle(self):
        return "Woof!"


class Chat(Animal):
    def __init__(self, nom):
        super().__init__(nom)

    def parle(self):
        return "Miaou!"


a = Animal("Patrick")
chat = Chat("Titi")
chien = Chien("Max")

print(chat.parle())
print(chien.parle())
a.parle()



