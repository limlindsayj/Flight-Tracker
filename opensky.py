from opensky_api import OpenSkyApi
from config import OPEN_SKY_ID, OPEN_SKY_SECRET, LONGITUDE, LATITUDE

class OpenSky:
    def __init__(self):
        self.api = OpenSkyApi(OPEN_SKY_ID, OPEN_SKY_SECRET)
        self.longitude = LONGITUDE
        self.latitude = LATITUDE
    
    def get_state_vector(self):
        #call the api and get the state vector 

    def get_flight_data(self, icao24):
        #call the api and get flight data based on icao24


    