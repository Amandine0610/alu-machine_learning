#!/usr/bin/env python3
import requests

def sentientPlanets():
    """
    Returns a list of home planet names of all sentient species.
    """
    url = "https://swapi.dev/api/species/"
    sentient_planets = set()

    while url:
        response = requests.get(url)
        if response.status_code != 200:
            break

        data = response.json()
        for species in data['results']:
            classification = species.get("classification", "").lower()
            designation = species.get("designation", "").lower()
            if "sentient" in classification or "sentient" in designation:
                homeworld_url = species.get("homeworld")
                if homeworld_url:
                    planet_response = requests.get(homeworld_url)
                    if planet_response.status_code == 200:
                        planet_data = planet_response.json()
                        name = planet_data.get("name")
                        if name:
                            sentient_planets.add(name)

        url = data.get("next")

    return sorted(sentient_planets)
