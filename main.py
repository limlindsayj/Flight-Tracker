from openskyclass import OpenSky
from config import get_token

def main():
    print("hello world")
    token = get_token()
    print(token)
    api = OpenSky(token)
    api.get_state_vectors()


if __name__ == "__main__":
    main()