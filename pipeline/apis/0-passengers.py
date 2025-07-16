#!/usr/bin/env python3
"""
    Returns a list of ship names that can hold at least `passengerCount` passengers.
    """

import requests

def availableShips(passengerCount):
    url = "https://swapi.dev/api/starships/"
    ships = []

    while url:
        response = requests.get(url)
        if response.status_code != 200:
            break  # Skip if response fails

        data = response.json()
        results = data.get("results", [])

        for ship in results:
            passengers = ship.get("passengers", "0").replace(",", "").split()[0]  # Strip commas and extra text
            try:
                if int(passengers) >= passengerCount:
                    ships.append(ship["name"])
            except ValueError:
                continue  # Skip if passengers can't be converted to int

        url = data.get("next")

    return ships
