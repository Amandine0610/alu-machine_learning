#!/usr/bin/env python3


""" Return list of ships"""

import requests
import sys
import time

def get_user_location(api_url):
    try:
        # Send GET request to the provided GitHub API URL
        response = requests.get(api_url)
        
        # Check for rate limit exceeded (403 status code)
        if response.status_code == 403:
            # Get the rate limit reset time from headers
            reset_timestamp = int(response.headers.get('X-RateLimit-Reset', 0))
            # Calculate minutes until reset
            current_time = int(time.time())
            minutes_until_reset = (reset_timestamp - current_time) // 60
            print(f"Reset in {minutes_until_reset} min")
            return
        
        # Check if user exists (200 for success, 404 for not found)
        if response.status_code == 404:
            print("Not found")
            return
        
        # Check if request was successful
        if response.status_code == 200:
            user_data = response.json()
            # Get location, default to empty string if not available
            location = user_data.get('location', '')
            # Print location if it exists, otherwise print nothing
            if location:
                print(location)
            else:
                print("Not found")
        else:
            print("Not found")
            
    except requests.RequestException:
        print("Not found")

if __name__ == '__main__':
    # Check if URL argument is provided
    if len(sys.argv) != 2:
        print("Usage: ./2-user_location.py <GitHub API URL>")
        sys.exit(1)
    
    # Get the API URL from command line argument
    api_url = sys.argv[1]
    get_user_location(api_url)
