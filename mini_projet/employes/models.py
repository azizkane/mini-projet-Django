from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Employe(models.Model):
    POSTE = [
        ('MANAGER', 'Manager'),
        ('DEV', 'Developpeur'),
        ('RH', 'Ressources Humaines'),
        ('MARKETING', 'Responsable Marketing'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, default=None)
    poste = models.CharField(max_length=30, choices=POSTE)
    date_embauche = models.DateField()

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - {self.poste} (embauché le {self.date_embauche})"

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

class Conge(models.Model):
    CONGE = [
        ('PAYE', 'Congé payé'),
        ('MALADIE', 'Congé maladie'),
    ]

    STATUT = [
        ('IDLE', 'En attente'),
        ('APPROUVE', 'Approuvé'),
        ('REFUSE', 'Refusé'),
    ]

    employe = models.ForeignKey(User, on_delete=models.CASCADE, related_name='conges')
    type_conge = models.CharField(max_length=15, choices=CONGE)
    date_debut = models.DateField()
    date_fin = models.DateField()
    statut = models.CharField(max_length=15, choices=STATUT, default='IDLE')
    traite_par = models.ForeignKey(Dirigeant, on_delete=models.SET_NULL, null=True, blank=True, related_name='conges_traites')
    date_traitement = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Congé de {self.employe.get_full_name()} du {self.date_debut} au {self.date_fin}"

    def traiter_conge(self, dirigeant, nouveau_statut):
        if isinstance(dirigeant, Dirigeant):
            self.statut = nouveau_statut
            self.traite_par = dirigeant
            self.date_traitement = timezone.now()
            self.save()
        else:
            raise ValueError("Seul un dirigeant peut traiter une demande de congé.")
