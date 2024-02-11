#!/bin/bash

# Vérifier si Python est installé
sudo apt update
if ! command -v python3 &> /dev/null; then
    echo "Python n'est pas installé. Installation en cours..."
    sudo apt install python3 -y
fi

# Vérifier si pip est installé
if ! command -v pip3 &> /dev/null; then
    echo "pip n'est pas installé. Installation en cours..."
    sudo apt install python3-pip -y
fi

# Installer les dépendances de l'application
pip3 install -r requirements.txt

# Lancer l'application Flask
python3 app_flask.py