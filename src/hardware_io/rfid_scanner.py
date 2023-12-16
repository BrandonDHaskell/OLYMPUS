import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from argon2 import PasswordHasher

reader = SimpleMFRC522()
ph = PasswordHasher()

# Reads an RFID tag, hashes the ID and returns the hashed ID
def get_hashed_id():
    try:
        id, text = reader.read()
        hashed_id = ph.hash(str(id))
        return hashed_id
    except Exception as e:
        # TODO: add logging
        print("Error: ", e)