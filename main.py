"""
Refactored code from: https://github.com/Daniel-Alnasir/OLYMPUS

The purpose of this code is to implement an RFID scanner at the entrance
of doors so members can scan to get into the facility.

"""

# imports

# Global variables

# main

    # Initialize service objects
        
        # DB ITEMS

        # Initialize Database
            # TODO
        
        
        # UTILITY ITEMS

        # Initialize Service logger as Logger
            # TODO
        
        
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