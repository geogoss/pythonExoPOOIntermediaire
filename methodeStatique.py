'''
Créer une méthode statique
Le but de cet exercice est de transformer la méthode chante_pour afin de la rendre statique.

La méthode doit permettre de chanter Joyeux Anniversaire pour une personne définie par l'argument
envoyé au paramètre prenom.

Dans ce cas-ci, le script doit donc afficher Joyeux Anniversaire pour Paul (la méthode chante_pour ne
doit pas afficher le texte de la chanson mais juste le retourner).

Vous devez donc rendre la méthode statique et la modifier pour qu'elle affiche le texte contenu dans
l'attribut paroles de la classe Chanson, adapté pour le prénom Paul.
'''

class Chanson:

    paroles = """Joyeux anniversaire,
Joyeux anniversaire,
Joyeux anniversaire {prenom},
Joyeux anniversaire."""

    @staticmethod
    def chante_pour(prenom):
        return Chanson.paroles.format(prenom=prenom)


print(Chanson.chante_pour("Paul"))

