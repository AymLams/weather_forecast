# weather_forecast
API qui permet de récupérer les informations météoroliguqes suivantes: 
* Météo actuelle
* Prédictions météorologiques pour les 7 jours suivants. 

Voici les deux URLS à utiliser afin d'utiliser notre API: 
* /weather/current?location={city : Retourne la météo courante sur la ville passée en paramètre
* /weather/forecast?location={city}: Retourne une version condensée des prévisions météo sur la ville passée en paramètre

# Prérequis
Cette API a été développée sous Python (3.12) via le framework Flask. <br>
Il est donc nécessaire d'avoir <b>Python 3.12</b> d'installé sur votre machine. <br>
De même cette application utilise une base de données <b>PostgreSQL</b> il est alors nécessaire d'avoir une base de données accessible.

# Installation de l'environnement
Veuillez suivre ces différentes étapes afin de mettre en place l'environnement. <br>
Placez-vous dans le dossier où vous avez récupérer le code présent dans ce repot.<br>
<i><u>Environnement développé et testé sous MacOS</i></u>
* <b> python3 -m venv venv </b> (<i>Vous installez l'environnement virtuel)</i>
* <b> source venv/bin/activate </b> (<i>Vous activez l'environnement créé précédemment</i>)
* <b> pip install -r requirements.txt </b> (<i>Installation des librairies et des dépendances</i>)
* <b> Mettez à jour le "config.ini" selon votre configuration personnelle </b>
* <b> Utiliser le fichier "create_database.sql" afin d'initialiser votre environnement SQL </b>
* <b> flask --app api/app.py run </b> (<i>Lancement de votre API</i>)

# Testing
Afin d'effectuer les tests de votre API, effectuez les commandes suivantes:
* <b>source venvTest/bin/activate</b>
* <b>pytest --pyargs api</b>
