import os
import requests
from dotenv import load_dotenv

from app.services.utils import affichageVille

load_dotenv()   #-> charge les valeur de .env

API_KEY = os.getenv("API_KEY")
UNITS = os.getenv("UNITS")
DEFAULT_CITY = os.getenv("DEFAULT_CITY")
LANG = os.getenv("LANG")

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather_by_city(city_name : str) -> dict:
    params = {
        "q": city_name,
        "appid": API_KEY,
        "units": UNITS,
        "lang": LANG
    }
    try:
        response = requests.get(BASE_URL, params=params, timeout=5)
        response.raise_for_status()  # ⬅️ lève une erreur si le code HTTP != 200

        data = response.json()
        return weather_data(data)

    except requests.exceptions.HTTPError as http_err:
        # Erreurs spécifiques de l’API
        if response.status_code == 404:
            return {"error": f"Ville '{city_name}' introuvable. Vérifie l’orthographe."}
        elif response.status_code == 401:
            return {"error": "Clé API invalide ou non autorisée."}
        else:
            return {"error": f"Erreur HTTP ({response.status_code}) : {http_err}"}

    except requests.exceptions.Timeout:
        return {"error": "Le serveur météo met trop de temps à répondre."}

    except requests.exceptions.RequestException as e:
        # Pour toutes les autres erreurs (connexion, DNS, etc.)
        return {"error": f"Erreur de connexion : {e}"}

def weather_data(api_json: dict) -> dict:

    main = api_json.get("main", {})
    wind = api_json.get("wind", {})
    weather = api_json.get("weather", [{}])[0]

    return {
        "city": api_json.get("name"),
        "temperature": main.get("temp"),
        "humidity": main.get("humidity"),
        "weather_condition": weather.get("description"),
        "wind_speed": wind.get("speed")
    }