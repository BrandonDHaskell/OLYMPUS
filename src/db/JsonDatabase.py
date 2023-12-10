import os
import json
import uuid
from datetime import datetime

class JsonDatabase:
    # TODO - add a member_id to group RFIDs to a single member
    # TODO - create backup file on occasion
    
    def __init__(self, filepath):
        self.filepath = filepath
        self.data = self._load_data()

    # attempt to load the JSON file
    # if it doesn't exist, create a new empty file
    def _load_data(self):
        os.makedirs(os.path.dirname(self.filepath), exist_ok=True)
        try:
            with open(self.filepath, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            with open(self.filepath, 'w') as file:
                json.dump({}, file)
            return {}

    # Write to JSON file (aka save)
    def _save_data(self):
        with open(self.filepath, 'w') as file:
            json.dump(self.data, file)


    # Adds a new record to the JSON db
    # Ensure uniqueness across UUIDs and RFIDs
    def add_record(self, rfid, member_level, membership_status):
        # Check for existing RFID
        if any(record['rfid'] == rfid for record in self.data.values()):
            raise ValueError("RFID already exists.")
        
        new_id = str(uuid.uuid4())
        while new_id in self.data:
            new_id = str(uuid.uuid4())

        self.data[new_id] = {
            'obf_rfid': obf_rfid,
            'member_level': member_level,
            'membership_status': membership_status,
            'member_sponsor': member_sponsor,
            'last_activity': datetime.now().isoformat()
        }
        self._save_data()

    # Get a record by RFID
    def get_record_by_rfid(self, rfid):
        for record in self.data.values():
            if record['rfid'] == rfid:
                return record
        return None

    # Update an existing record
    def update_record(self, id, **kwargs):
        if id not in self.data:
            raise ValueError("Record not found.")
        self.data[id].update(kwargs)
        self.data[id]['last_activity'] = datetime.now().isoformat()
        self._save_data()
