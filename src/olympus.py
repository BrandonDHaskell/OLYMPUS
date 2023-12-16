"""
Refactored code from: https://github.com/Daniel-Alnasir/OLYMPUS

The purpose of this code is to implement an RFID scanner at the entrance
of doors so members can scan to get into the facility.

"""

# imports
import time
import RPi.GPIO as GPIO

from utils.Logger import create_logger
from db.JsonDatabase import JsonDatabase
from hardware_io.rfid_scanner import get_hashed_id
from hardware_io.toggle_switch import ToggleSwitch


# Global variables

# main
def main():
    # Initialize service

    # Logger
    logger = create_logger('Olympus')
    logger.info("Starting Olympus...")

    # Database
    db = JsonDatabase('db/data/RfidDb.json')
    logger.info("Database initialized...")

    door_open_status_switch = ToggleSwitch(3, 'input')
    last_door_state = None

    # Temp Testing
    # try:
    #     db.add_record('rfid1234', 'admin', 'new')
    # except ValueError as e:
    #     logger.error("Error adding record: %s", e)

    # record = db.get_record_by_rfid('rfid1234')
    # logger.info('%s', record)

    # try:
    #     db.add_record('rfid2345', 'admin', 'new')
    # except ValueError as e:
    #     logger.error("Error adding record: %s", e)

    # record = db.get_record_by_rfid('rfid2345')
    # logger.info('%s', record)


    # Initialize service objects
        
        # HARDWARE ITEMS
        
        # Initialize RFID Scanner as Scanner
            # TODO
        # Initialize Door latch as Door
            # TODO
        # Initialize Member Mod Switch (Button) as Add_Member_State
            # TODO
        # Initialize Member scan Button (Button) as Scan_Member_State
            # TODO
        # Initialize LCD Screen as Screen
            # TODO


    # Begin service loop
    while True:
        current_door_state = door_open_status_switch.read()

        # Test an only update if status changes
        if current_door_state != last_door_state:
            if current_door_state == GPIO.HIGH:
                print("Door closed")
                # TODO handle door open event
            else:
                print("Door closed")
                # TODO handle door close event

            # Update last state
            last_door_state = current_door_state
        
        time.sleep(7)

        # Get Add_Member_State status
        # If Add_Member_State == False (Switch Off)
            # Ping for RFID response (Scanner.scan())
                # TODO
            # If RFID signal detected (Scanner.read())
                # Get card data
                    # TODO
                # Log access request record
                    # TODO
                # Get member data object from DB
                    # TODO
                # If data object exists (aka Member has DB record)
                    # Get Member status from DB object
                        # TODO
                    # If Member is Active
                        # Log access granted record
                            # TODO
                        # Update DB with recent activity
                            # TODO
                        # Unlatch door for X seconds
                            # TODO
                        # Write status to LCD
                            # TODO
                    # If Member is Paused
                        # Log access denied record
                            # TODO
                        # Write status to LCD
                            # TODO
                    # Else (Unknown Member State)
                        # Log access denied record
                            # TODO
                        # Write status to LCD
                            # TODO
                # Else (No data object)
                    # Log access denied record
                        # TODO
                    # Write status to LCD
                        # TODO
        # Else (Add_Member_State == True)
            # Log add member enabled
                # TODO
            # If member_card_data == null or guest_card_data == null
                # Get Scan_Member_State status
                    # TODO
                # If Scan_Member_State == False
                    # Write status to LCD: Scan guest
                        # TODO
                    # Get card data (Scanner.read()) and create guest_card_data object
                        # TODO
                    # Log guest scan record
                        # TODO
                # Else (Scan_Member_State == True)
                    # Write status to LCD: Scan member
                        # TODO
                    # Get card data (Scanner.read()) and create member_card_data object
                        # TODO
                    # Log guest scan record
                        # TODO
            # Else (Card data has been scanned for member and guest)
                # Loop
                    # Check if guest is already in DB
                        # TODO
                    # If guest DB record == null
                        # Validate member status
                            # TODO
                        # If Member DB record != null and (Member.status == "Member" or Member.status == "Admin")
                            # Add guest to database
                                # TODO
                            # Log guest update record
                                # TODO
                            # Set member_card_data == null
                                # TODO
                            # Set guest_card_data == null
                                # TODO
                            # Write status to LCD: Guest added
                                # TODO
                        # Else (Sponsor not Authorized)
                            # Log guest creation denied
                                # TODO
                            # Set member_card_data == null
                                # TODO
                            # Set guest_card_data == null
                                # TODO
                            # Write status to LCD: Sponsor not Authorized
                                # TODO
                    # Else (guest DB record exists)
                        # Log guest creation stopped record
                            # TODO
                        # Write status to LCD: Guest already exists
                            # TODO
                # End loop
    # End Service loop

if __name__ == "__main__":
    main()