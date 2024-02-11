from flask import Flask
import requests

app = Flask(__name__)


@app.route("/")
def get_date():
    # URL de l'API de l'horloge mondiale pour obtenir la date actuelle
    api_url = "http://worldclockapi.com/api/json/utc/now"

    # Faire une requête GET vers l'API
    response = requests.get(api_url)

    # Vérifier si la requête a réussi
    if response.status_code == 200:
        # Récupérer la date actuelle depuis la réponse JSON
        current_date = response.json()["currentDateTime"]
        return f"Aujourd'hui, nous sommes le {current_date}"
    else:
        return "Impossible de récupérer la date actuelle."


if __name__ == "__main__":
    app.run(host="0.0.0.0")
