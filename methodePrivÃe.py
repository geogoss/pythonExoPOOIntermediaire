'''
Rendre une méthode privée
La classe  MachineACafe permet de faire du café et dispose pour ce faire de trois méthodes :

chauffe_eau
moud_cafe
fait_du_cafe

Dans le code de départ, ces trois méthodes sont accessibles directement par l'instance.

Cependant, on aimerait restreindre l'accès aux méthodes chauffe_eau et moud_cafe qui n'ont pas vocation à
être utilisée directement par l'utilisateur mais uniquement par la méthode fait_du_cafe.

Vous devez donc rendre ces deux méthodes privées et adapter le code de la méthode fait_du_cafe pour utiliser
ces méthodes privées.
'''

class MachineACafe:
    def __init__(self):
        self.temperature_eau = 0

    def __chauffe_eau(self):
        self.temperature_eau = 100
        print("L'eau est chaude.")

    def __moud_cafe(self):
        print("Café moulu avec succès.")

    def fait_du_cafe(self):
        self.__moud_cafe()
        self.__chauffe_eau()
        print("Le café est prêt")


machine = MachineACafe()
machine.fait_du_cafe()
# ce dernier ne fonctionnera pas car méthode est maintenant privée
machine.__moud_cafe()


print("Hello baby")