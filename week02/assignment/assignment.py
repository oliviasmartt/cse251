"""
Course: CSE 251 
Lesson Week: 02
File: assignment.py 
Author: Olivia Smart

Purpose: Retrieve Star Wars details from a server

Instructions:

- Each API call must only retrieve one piece of information
- You are not allowed to use any other modules/packages except for the ones used
  in this assignment.
- Run the server.py program from a terminal/console program.  Simply type
  "python server.py"
- The only "fixed" or hard coded URL that you can use is TOP_API_URL.  Use this
  URL to retrieve other URLs that you can use to retrieve information from the
  server.
- You need to match the output outlined in the decription of the assignment.
  Note that the names are sorted.
- You are requied to use a threaded class (inherited from threading.Thread) for
  this assignment.  This object will make the API calls to the server. You can
  define your class within this Python file (ie., no need to have a seperate
  file for the class)
- Do not add any global variables except for the ones included in this program.

The call to TOP_API_URL will return the following Dictionary(JSON).  Do NOT have
this dictionary hard coded - use the API call to get this.  Then you can use
this dictionary to make other API calls for data.

{
   "people": "http://127.0.0.1:8790/people/", 
   "planets": "http://127.0.0.1:8790/planets/", 
   "films": "http://127.0.0.1:8790/films/",
   "species": "http://127.0.0.1:8790/species/", 
   "vehicles": "http://127.0.0.1:8790/vehicles/", 
   "starships": "http://127.0.0.1:8790/starships/"
}
"""

from datetime import datetime, timedelta
import requests
import json
import threading

# Include cse 251 common Python files
from cse251 import *

# Const Values
TOP_API_URL = 'http://127.0.0.1:8790'

# Global Variables
call_count = 0


# Threaded Class Definition
class APICallThread(threading.Thread):
    def __init__(self, url):
        super().__init__()
        self.url = url
        self.result = None 

    def run(self):
        global call_count
        response = requests.get(self.url)
        self.result = response.json()
        call_count += 1


def main():
    log = Log(show_terminal=True)
    log.start_timer('Starting to retrieve data from the server')

    top_api_thread = APICallThread(TOP_API_URL)
    top_api_thread.start()
    top_api_thread.join()
    top_api_urls = top_api_thread.result  # Access the result of the API call

    film_6_thread = APICallThread(top_api_urls['films'] + '6/')
    film_6_thread.start()
    film_6_thread.join()
    film_6_details = film_6_thread.result

    characters = []
    for character_url in film_6_details["characters"]:
        character_thread = APICallThread(character_url)
        character_thread.start()
        character_thread.join()
        character_details = character_thread.result
        characters.append(character_details["name"])

    planets = []
    for planet_url in film_6_details["planets"]:
        planet_thread = APICallThread(planet_url)
        planet_thread.start()
        planet_thread.join()
        planet_details = planet_thread.result
        planets.append(planet_details["name"])

    # Retrieve and display details of starships
    starships = []
    for starship_url in film_6_details["starships"]:
        starship_thread = APICallThread(starship_url)
        starship_thread.start()
        starship_thread.join()
        starship_details = starship_thread.result
        starships.append(starship_details["name"])

    vehicles = []
    for vehicle_url in film_6_details["vehicles"]:
        vehicle_thread = APICallThread(vehicle_url)
        vehicle_thread.start()
        vehicle_thread.join()
        vehicle_details = vehicle_thread.result
        vehicles.append(vehicle_details["name"])

    # Get and display details of species
    species = []
    for species_url in film_6_details["species"]:
        species_thread = APICallThread(species_url)
        species_thread.start()
        species_thread.join()
        species_details = species_thread.result
        species.append(species_details["name"])

    # Display results
    log.write('Details of Film 6:')
    log.write(f'Title: {film_6_details["title"]}')
    log.write(f'Director: {film_6_details["director"]}')
    log.write(f'Release Date: {film_6_details["release_date"]}')
    log.write(f'Producer: {film_6_details["producer"]}')
    log.write('Characters:')
    for character in characters:
        log.write(f'- {character}')
    log.write('Planets:')
    for planet in planets:
        log.write(f'- {planet}')
    log.write('Starships:')
    for starship in starships:
        log.write(f'- {starship}')
    log.write('Vehicles:')
    for vehicle in vehicles:
        log.write(f'- {vehicle}')
    log.write('Species:')
    for specie in species:
        log.write(f'- {specie}')

    log.stop_timer('Total Time To complete')
    log.write(f'There were {call_count} calls to the server')


if __name__ == "__main__":
    main()
