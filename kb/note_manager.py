import json
import os

DATA_FILE = "data/notes.json"

class NoteManager:
    def __init__(self):
        os.makedirs("data", exist_ok=True)
        if not os.path.exists(DATA_FILE):
            with open(DATA_FILE, "w") as f:
                json.dump([], f)

    def add_note(self, title, content):
        notes = self.get_notes()
        note = {
            "id": len(notes) + 1,
            "title": title,
            "content": content
        }
        notes.append(note)

        with open(DATA_FILE, "w") as f:
            json.dump(notes, f, indent=4)

        print("Note added successfully.")

    def get_notes(self):
        with open(DATA_FILE, "r") as f:
            return json.load(f)