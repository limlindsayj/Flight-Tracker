from opensky_api import OpenSkyApi
from config import LONGITUDE, LATITUDE
import requests

class OpenSky:
    def __init__(self, token):
        self.headers = {"Authorization": f"Bearer {token}"}
        self.api_url = "https://opensky-network.org/api/"

    def get_flight_data(self, time, icao24):
        begin_time = time - 72000
        end_time = time + 72000
        flight_data_url = f"https://opensky-network.org/api/flights/aircraft?begin={begin_time}&end={end_time}&icao24={icao24}"
        print(flight_data_url)
        res = requests.get(flight_data_url, headers=self.headers)
        if not res.json():
            return ""
        data = res.json()[0]
        return f"Departing from: {data['estDepartureAirport']}, Arriving at: {data['estArrivalAirport']}"
    
    def get_state_vectors(self):
        #swiss airspace
        state_url = self.api_url + "states/all?lamin=45.8389&lomin=5.9962&lamax=47.8229&lomax=10.5226"
        res = requests.get(state_url, headers=self.headers).json()
        states = res['states']
        time = res['time']
        print(states)
        CALLSIGN_INDEX = 1
        ICAO24_INDEX = 0
        for state in states:
            print(state[CALLSIGN_INDEX])
            print(" " + self.get_flight_data(time, state[ICAO24_INDEX]))
    