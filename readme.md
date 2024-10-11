
# Gestion d'Entreprise - Application Django

## À propos du projet

Ce projet est une petite application Django conçue pour apprendre et pratiquer le développement web avec Django. L'application se concentre sur la gestion des employés, des dirigeants et des congés au sein d'une entreprise.

## Fonctionnalités principales

- Gestion des employés et des dirigeants
- Système de demande et d'approbation de congés
- API RESTful pour accéder aux données
- Gestion des droits d'utilisateurs

## Installation

1. Créez un environnement virtuel :

python -m venv env
source env/bin/activate  # Sur Windows, utilisez `env\Scripts\activate`


2. Installez les dépendances :

pip install django djangorestframework


3. Clonez le projet et naviguez dans le dossier :

git clone [https://github.com/azizkane/mini-projet-Django.git]
cd gestion_entreprise


1. Appliquez les migrations :

python manage.py migrate


5. Lancez le serveur de développement :

python manage.py runserver


## Structure du projet

Le projet est organisé comme suit :

- `employes` : Application Django pour la gestion des employés et des congés
- `gestion_entreprise` : Dossier principal du projet **Django**SonarService.bat

## API Endpoints

- `/api/employes/` : Liste et création d'employés
- `/api/dirigeants/` : Liste et création de dirigeants
- `/api/conges/` : Liste, création et gestion des congés

## Apprentissage et développement

Ce projet a été créé dans le but d'apprendre et de pratiquer les concepts suivants :

- Création de modèles Django et relations entre eux
- Mise en place d'une API RESTful avec Django REST Framework
- Gestion des permissions et des droits d'utilisateurs
- Utilisation de filtres dans l'API
- Configuration de l'authentification (Token ou JWT)

N'hésitez pas à explorer le code, expérimenter avec les fonctionnalités et étendre le projet pour approfondir vos connaissances en développement Django !
