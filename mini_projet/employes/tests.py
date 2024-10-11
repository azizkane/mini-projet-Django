from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Employe, Dirigeant, Conge
from datetime import date

class EmployeTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.employe_data = {
            'nom': 'Doe',
            'prenom': 'John',
            'poste': 'DEV',
            'email': 'john@example.com',
            'date_embauche': '2023-01-01'
        }
        self.employe = Employe.objects.create(**self.employe_data)

    def test_create_employe(self):
        new_employe_data = {
            'nom': 'Smith',
            'prenom': 'Jane',
            'poste': 'RH',
            'email': 'jane@example.com',
            'date_embauche': '2023-02-01'
        }
        response = self.client.post(reverse('employe-list'), new_employe_data, format='json')
        if response.status_code != status.HTTP_201_CREATED:
            print(response.content)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_read_employe(self):
        response = self.client.get(reverse('employe-detail', kwargs={'pk': self.employe.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_employe(self):
        updated_data = {**self.employe_data, 'nom': 'Smith'}
        response = self.client.put(reverse('employe-detail', kwargs={'pk': self.employe.pk}), updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_employe(self):
        response = self.client.delete(reverse('employe-detail', kwargs={'pk': self.employe.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class DirigeantTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.employe = Employe.objects.create(nom='Doe', prenom='Jane', poste='MANAGER', email='jane@example.com', date_embauche='2023-01-01')
        self.dirigeant_data = {
            'employe': self.employe,
            'nombre_employes_supervises': 5
        }
        self.dirigeant = Dirigeant.objects.create(**self.dirigeant_data)

    def test_create_dirigeant(self):
        new_employe = Employe.objects.create(nom='Smith', prenom='John', poste='MANAGER', email='john@example.com', date_embauche='2023-02-01')
        new_dirigeant_data = {
            'employe': new_employe.id,
            'nombre_employes_supervises': 3
        }
        response = self.client.post(reverse('dirigeant-list'), new_dirigeant_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_read_dirigeant(self):
        response = self.client.get(reverse('dirigeant-detail', kwargs={'pk': self.dirigeant.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_dirigeant(self):
        updated_data = {'nombre_employes_supervises': 10}
        response = self.client.patch(reverse('dirigeant-detail', kwargs={'pk': self.dirigeant.pk}), updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_dirigeant(self):
        response = self.client.delete(reverse('dirigeant-detail', kwargs={'pk': self.dirigeant.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class CongeTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.employe = Employe.objects.create(nom='Doe', prenom='Bob', poste='DEV', email='bob@example.com', date_embauche='2023-01-01')
        self.conge_data = {
            'employe': self.employe,
            'type_conge': 'PAYE',
            'date_debut': '2023-07-01',
            'date_fin': '2023-07-15',
            'statut': 'IDLE'
        }
        self.conge = Conge.objects.create(**self.conge_data)

    def test_create_conge(self):
        new_employe = Employe.objects.create(nom='Smith', prenom='Alice', poste='RH', email='alice@example.com', date_embauche='2023-03-01')
        new_conge_data = {
            'employe': new_employe.id,
            'type_conge': 'MALADIE',
            'date_debut': '2023-08-01',
            'date_fin': '2023-08-05',
            'statut': 'IDLE'
        }
        response = self.client.post(reverse('conge-list'), new_conge_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_read_conge(self):
        response = self.client.get(reverse('conge-detail', kwargs={'pk': self.conge.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_conge(self):
        updated_data = {'statut': 'APPROUVE'}
        response = self.client.patch(reverse('conge-detail', kwargs={'pk': self.conge.pk}), updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_conge(self):
        response = self.client.delete(reverse('conge-detail', kwargs={'pk': self.conge.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
