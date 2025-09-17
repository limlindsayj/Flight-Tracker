import os
from dotenv import load_dotenv
import requests

load_dotenv()

OPEN_SKY_ID = os.getenv("OPEN_SKY_ID")
OPEN_SKY_SECRET = os.getenv("OPEN_SKY_SECRET")

LONGITUDE = os.getenv("LONGITUDE")
LATITUDE = os.getenv("LATITUDE")

def get_token():
    url = "https://auth.opensky-network.org/auth/realms/opensky-network/protocol/openid-connect/token"

    data = {
        "grant_type": "client_credentials",
        "client_id": OPEN_SKY_ID,
        "client_secret": OPEN_SKY_SECRET
    }

    response = requests.post(url, data=data)
    token = response.json().get("access_token")
    return token
