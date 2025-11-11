import argparse
import os

from app.services.meteo_api import get_weather_by_city
from app.services.utils import affichageVille

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("ville", default = os.getenv("DEFAULT_CITY"), nargs="?")
    args = parser.parse_args()
    meteo = get_weather_by_city(args.ville)

    print("========== Météo Tracker ==========\n")
    print(affichageVille(meteo))

if __name__ == "__main__":
    main()