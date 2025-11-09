def affichageVille(data: dict) -> str:


    if "error" in data:
        return f"Erreur : {data['error']}"

    city = data.get("city")
    temp = data.get("temperature")
    humidity = data.get("humidity")
    condition = data.get("weather_condition", "Non précisé")
    wind_speed = data.get("wind_speed") * 3.6  # conversion m/s → km/h

    res = f"À {city}, il fait environ {round(temp)}°C avec un ciel {condition}.\n"
    res += f"L'humidité est de {humidity}% et le vent souffle à environ {round(wind_speed)} km/h.\n"

    return res
