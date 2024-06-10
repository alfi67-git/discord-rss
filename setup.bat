:: Créer un environnement virtuel
python -m venv discord-rss

:: Activer l'environnement virtuel
call discord-rss\Scripts\activate

:: Installer les dépendances
pip install -r requirements.txt

:: Exécuter le script principal
python main.py
