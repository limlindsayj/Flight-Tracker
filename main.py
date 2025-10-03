import api
from config import get_token
#import requests

def main():
    token = get_token()
    api.create_flights(token)


if __name__ == "__main__":
    main()