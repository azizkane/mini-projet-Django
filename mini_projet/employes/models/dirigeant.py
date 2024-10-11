from django.db import models
from .employe import Employe


# Méthode 1: Associer Dirigeant à Employe en utilisant un champ OneToOneField
class Dirigeant(models.Model):
    employe = models.OneToOneField(Employe, on_delete=models.CASCADE)
    nombre_employes_supervises = models.PositiveIntegerField(default=0, help_text="Nombre d'employés supervisés par le dirigeant")
    def __str__(self):
        return f"Dirigeant: {self.employe}"

# Méthode 2: Associer Dirigeant à Employe par une relation de rôle
# class Dirigeant(models.Model):
#     employe = models.ForeignKey(Employe, on_delete=models.CASCADE)
#     est_dirigeant = models.BooleanField(default=True)
#     # Ajoutez ici des champs supplémentaires spécifiques aux dirigeants si nécessaire
#
#     def __str__(self):
#         return f"Dirigeant: {self.employe}"