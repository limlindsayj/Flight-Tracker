from opensky_api import OpenSkyApi
from config import LAMIN, LAMAX, LOMIN, LOMAX, GC_KEY, GC_ID
import requests
from flight_data import FlightData

ICAO24_INDEX = 1
COMMERCIAL_CATEGORIES = set(range(3, 7))
OPENSKY_URL = "https://opensky-network.org/api/"
GC_URL = "https://www.googleapis.com/customsearch/v1"
    
def get_state_vectors(token):
    state_url = f"{OPENSKY_URL}states/all?lamin={LAMIN}&lamax={LAMAX}&lomin={LOMIN}&lomax={LOMAX}"
    res = requests.get(state_url, headers={"Authorization": f"Bearer {token}"}).json()
    states = res['states']
    return states

def get_flight_data(icao):
    params = {
        "key": GC_KEY,
        "cx": GC_ID,
        "q": f"{icao}+flight+schedule",
        "num": 1
    }

    response = requests.get(GC_URL, params=params)
    data = response.json()
    if "items" in data:
        metatags = data["items"][0]["pagemap"]["metatags"][0]
        departure = "Unknown" if not "origin" in metatags else metatags["origin"]
        arrival = "Unknown" if not "destination" in metatags else metatags["destination"]
        description = "Unknown" if not "twitter:description" in metatags else metatags["twitter:description"][6:]
    else:
        departure = "Unknown"
        arrival = "Unknown"
        description = "Unknown"
    return FlightData(icao, departure, arrival, description)

def create_flights(token):
    flights = []
    states = get_state_vectors(token)
    for state in states:
        flight_data = get_flight_data(state[ICAO24_INDEX])
        print(flight_data)
    