import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import hashlib

reader = SimpleMFRC522()

# Reads an RFID tag, hashes the ID and returns the hashed ID
def get_hashed_id():
    try:
        id, text = reader.read()
        if (id):
            hashed_id = hashlib.sha3_256(str(id).encode()).hexdigest()
            return hashed_id
        else:
            return None
    except Exception as e:
        # TODO: add logging
        print("Error: ", e)