from RPLCD.i2c import CharLCD
import time 

lcd = CharLCD('PCF8574', 0x27)

lcd.write_string("Hello, World!")

def write_lcd(string):
    lcd.write_string(string)