#!/usr/bin/env python3
"""
Script to display the upcoming SpaceX launch information
using the unofficial SpaceX API
"""

import requests
from datetime import datetime



def get_upcoming_launch():
    """
    Fetches the upcoming SpaceX launch information from the API
    Returns formatted string with launch details
    """
    try:
        # Get all upcoming launches
        launches_url = "https://api.spacexdata.com/v4/launches/upcoming"
        launches_response = requests.get(launches_url)
        launches_response.raise_for_status()
        launches = launches_response.json()
        
        if not launches:
            return "No upcoming launches found"
        
        # Sort by date_unix to get the soonest launch
        # If date_unix is None, treat as far future for sorting
        launches.sort(key=lambda x: x.get('date_unix', float('inf')))
        upcoming_launch = launches[0]
        
        # Get rocket information
        rocket_id = upcoming_launch['rocket']
        rocket_url = "https://api.spacexdata.com/v4/rockets/{}".format(rocket_id)
        rocket_response = requests.get(rocket_url)
        rocket_response.raise_for_status()
        rocket = rocket_response.json()
        rocket_name = rocket['name']
        
        # Get launchpad information
        launchpad_id = upcoming_launch['launchpad']
        launchpad_url = "https://api.spacexdata.com/v4/launchpads/{}".format(launchpad_id)
        launchpad_response = requests.get(launchpad_url)
        launchpad_response.raise_for_status()
        launchpad = launchpad_response.json()
        launchpad_name = launchpad['name']
        launchpad_locality = launchpad['locality']
        
        # Format the date in local time
        # Convert from UTC to local timezone
        if upcoming_launch.get('date_unix'):
            utc_time = datetime.fromtimestamp(upcoming_launch['date_unix'], tz=pytz.UTC)
            local_time = utc_time.astimezone()
            date_str = local_time.strftime("%Y-%m-%dT%H:%M:%S%z")
            # Format timezone offset correctly (add colon)
            if len(date_str) >= 5 and date_str[-5] in ['+', '-']:
                date_str = date_str[:-2] + ':' + date_str[-2:]
        else:
            # Fallback to ISO string if date_unix is not available
            date_str = upcoming_launch.get('date_local', 'TBD')
        
        # Get launch name
        launch_name = upcoming_launch.get('name', 'Unknown')
        
        # Format the output
        result = "{} ({}) {} - {} ({})".format(
            launch_name, date_str, rocket_name, launchpad_name, launchpad_locality
        )
        return result
        
    except requests.exceptions.RequestException as e:
        return "Error fetching data: {}".format(e)
    except KeyError as e:
        return "Error parsing data: Missing field {}".format(e)
    except Exception as e:
        return "Unexpected error: {}".format(e)


if __name__ == '__main__':
    print(get_upcoming_launch())
