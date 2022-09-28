'''
Supprimer une instance
Dans cet exercice, nous voulons récupérer dans une liste etudiants_partis les étudiants qui ne sont plus
présents dans notre établissement scolaire.

Pour cela, nous souhaitons permettre la suppression d'une instance de la classe Etudiant.

Lors de la suppression de l'instance, le prénom et le nom de l'étudiant en question doivent être ajoutés à la
liste etudiants_partis.

Dans ce cas-ci, la liste etudiants_partis doit donc à la fin du script être égale à ["Marc Tremblay"].
'''

etudiants_partis = []


class Etudiant:
    def __init__(self, prenom, nom):
        self.prenom = prenom
        self.nom = nom

    def __del__(self):
        etudiants_partis.append(f"{self.prenom} {self.nom}")

john = Etudiant("John", "Smith")
julie = Etudiant("Julie", "Martin")
marc = Etudiant("Marc", "Tremblay")


print(marc.nom)

del marc
print(etudiants_partis)





