

# Pencil Project


## Auteurs
- Author 1 : LABDOUNI Amira
- Author 2 : MEKHALDI HANNAH

**Version :** 27/01/2025

## Description du projet

Ce projet modélise un système de gestion pour une industrie de fabrication de crayons. En s'appuyant sur Django, il intègre la gestion de diverses entités telles que les villes, les locaux, les usines, et les ressources nécessaires à la production.

**Objectifs :** 
- Construire des modèles en Python/Django pour représenter les entités.
- Mettre en place une interface pour les visualiser sur localhost:8000/ grâce à une DetailView et une méthode json().
- Étendre les fonctionnalités avec une ApiView en ajoutant une méthode json_extended().
- Développer un outil en C++ permettant de lire et afficher ces données directement dans un terminal.

## Environnement et prérequis 

**Environnement de développement:** Le projet a été développé sous Ubuntu 20.04 avec :

- Python 3
- Pip
- Git
- Venv (environnement virtuel Python)
- WSL Ubuntu (si Windows est utilisé)

Assurez-vous d'avoir les éléments ci-dessus installés sur votre machine.

## Guide d'installation

## Commandes pour les installations :

```bash
# Mettre a jour la liste des paquets
sudo apt update

# Installation de Python 3
sudo apt install python3

# Verification de l'installation de pip
python3 -m pip -V

# Installation de git
sudo apt install git

# Installation de venv (virtual environement)
sudo apt install python3-venv

``` 
## Démarrage


### 1. Cloner le dépôt GitHub : 
```bash
git clone https://github.com/NiiteeZ/Projet_Crayon.git

```

### 2. Se placer dans le dossier: 
```bash
cd Projet_crayon/
```

### 3. Configuration de l'environnement virtuel :

**Créez un environnement virtuel :**
```bash
python3 -m venv .venv
echo .venv >> .gitignore
```
**Activez-le selon votre système :**
```bash
#  Linux/Mac :

source .venv/bin/activate

#  Windows :

.venv\Scripts\activate

```
### 4. Installation des dépendances:

Mettez à jour pip et installez Django pour votre projet :

```bash
pip install -U pip
pip install django
```

## Lancement du serveur Django







```bash

```
