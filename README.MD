# Installation et initialisation de projets Flask Python


## Installation de Flask pour Visual Studio

Pour visual studio code
Python3 -m venv vent
. env/bin/activate
Pip3 install Flask

## Pour PyCharm

créer un nouveau projet Flask

## Installation de SQLAlchemy pour SQL LITE
pip install Flask-SQLAlchemy

suppression des data dans dataInit car la base de données gère les données maintenant
.

Taper les commandes suivantes dans le shell de Flask
Flask shell
from app import db
db.create_all()

et enfin dans la console flask run

## Migrations

installer FLask-Migrate: pip install Flask-Migrate

puis taper: flask db init

supprimer la base de donnée 

flask db migrate

et 

flask db upgrade

En cas de changements de table refaire ensuite 

flask db migrate et flask db upgrade
