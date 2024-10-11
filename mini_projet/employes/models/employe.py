from django.db import models
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