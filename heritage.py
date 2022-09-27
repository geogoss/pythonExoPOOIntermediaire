'''
Éviter la répétition avec l'héritage
Dans cet exercice, vous devez simplifier le code grâce à l'héritage.

En effet, dans l'état actuel du script, on répète plusieurs fois les informations de nom et prenom de
nos personnages.

Ça fonctionne, mais ce n'est pas très efficace.

Vous devez donc créer une classe Personnage dont vont hériter les classes Magicien, Gobelin et Chevalier.

Cette classe Personnage devra définir les attributs nom et prenom qui sont communs aux trois classes.

Vous ne devez pas toucher à l'attribut puissance des classes Magicien, Gobelin et Chevalier.

Ces trois classes devront donc avoir un attribut puissance égal respectivement à 80, 20 et 70.
'''

class Personnage:
    def __init__(self, nom, prenom):
        self.prenom = prenom
        self.nom = nom


class Magicien(Personnage):
    def __init__(self, prenom, nom):
        super().__init__(prenom, nom)
        self.puissance = 80

    def __str__(self):
        return f"Magicien {self.nom} {self.prenom} possède une puissance de {self.puissance}"

class Gobelin(Personnage):
    def __init__(self, prenom, nom):
        super().__init__(prenom, nom)
        self.puissance = 20

    def __str__(self):
        return f"Gobelin {self.nom} {self.prenom} possède une puissance de {self.puissance}"

class Chevalier(Personnage):
    def __init__(self, prenom, nom):
        super().__init__(prenom, nom)
        self.puissance = 70

    def __str__(self):
        return f"Chevalier {self.nom} {self.prenom} possède une puissance de {self.puissance}"

perso1 = Magicien("maitre", "gandalf")
print(perso1)
print(perso1.puissance)

perso2 = Gobelin("Petit", "Nain")
print(perso2)
print(perso2.puissance)

perso3 = Chevalier("Geoffrey", "Gosset")
print(perso3)
print(perso3.puissance)

