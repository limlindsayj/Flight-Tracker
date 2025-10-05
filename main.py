import api
from config import get_token
from lcd_test import write_lcd
def main():
    token = get_token()
    flights = api.create_flights(token)
    write_lcd(flights[0])



if __name__ == "__main__":
    main()