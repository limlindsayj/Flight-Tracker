from RPLCD.i2c import CharLCD

# Adjust '0x27' if your i2cdetect shows a different address
lcd = CharLCD('PCF8574', 0x27)

lcd.write_string("Hello, World!")

