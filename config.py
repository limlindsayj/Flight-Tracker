import os
from dotenv import load_dotenv

load_dotenv()

OPEN_SKY_ID = os.getenv("OPEN_SKY_ID")
OPEN_SKY_SECRET = os.getenv("OPEN_SKY_SECRET")

LONGITUDE = os.getenv("LONGITUDE")
LATITUDE = os.getenv("LATITUDE")