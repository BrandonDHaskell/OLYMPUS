import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from argon2 import PasswordHasher

reader = SimpleMFRC522()
ph = PasswordHasher()

# Reads an RFID tag, hashes the ID and returns the hashed ID
def get_hashed_id():
    try:
        # Check for presence of RFID tag
        (status, tag_type) = reader.request(reader.REQIDL)
        
        # if card is present, scan, else return nothing
        if status == reader.OK:

            id, text = reader.read()
            hashed_id = ph.hash(str(id))
            return hashed_id
        else:
            return None
    except Exception as e:
        # TODO: add logging
        print("Error: ", e)
    finally:
        GPIO.cleanup()