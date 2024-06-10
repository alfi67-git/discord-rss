#!/bin/bash

# Créer un environnement virtuel
python3 -m venv discord-rss

# Activer l'environnement virtuel
source discord-rss/bin/activate

# Installer les dépendances
pip install -r requirements.txt

# Exécuter le script principal
python main.py
