#!/bin/bash

# Installe tous les packages nécessaires
sudo apt install python3.11-venv
sudo apt install pip
echo "##########  Tous les packages ont été installés..."

# Créer un environnement virtuel
python3 -m venv discord-rss
echo "##########  Environnement virtuel créer..."

# Activer l'environnement virtuel
source discord-rss/bin/activate
echo "##########  Environnement virtuel activé..."

# Installer les dépendances
pip install -r requirements.txt
echo "##########  Dépendances installées..."

# Exécuter le script principal
python main.py
