from django import forms
from .models import Conge

class CongeEmployeForm(forms.ModelForm):
    class Meta:
        model = Conge
        fields = ['type_conge', 'date_debut', 'date_fin']

class CongeDirigeantForm(forms.ModelForm):
    class Meta:
        model = Conge
        fields = ['type_conge', 'date_debut', 'date_fin', 'statut', 'traite_par', 'date_traitement']
