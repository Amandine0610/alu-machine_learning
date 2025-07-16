#!/usr/bin/env python3
import requests

def availableShips(passengerCount):
    """
    Returns a list of ship names that can hold at least `passengerCount` passengers.
    """
    url = "https://swapi.dev/api/starships/"
    ships = []

    while url:
        response = requests.get(url)
        if response.status_code != 200:
            break  # If something goes wrong, exit the loop

        data = response.json()
        for ship in data['results']:
            passengers = ship.get('passengers', '0').replace(',', '').replace('n/a', '0').replace('unknown', '0')
            try:
                if int(passengers) >= passengerCount:
                    ships.append(ship['name'])
            except ValueError:
                continue  # Skip entries with non-numeric passengers

        url = data.get('next')

    return ships
