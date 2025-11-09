# utils/helpers.py
import json
from pathlib import Path


MAPPINGS_PATH = Path('data/mappings.json')




def load_mappings():
    if MAPPINGS_PATH.exists():
        return json.loads(MAPPINGS_PATH.read_text())
    return {}




def save_mappings(mappings):
    MAPPINGS_PATH.parent.mkdir(parents=True, exist_ok=True)
    MAPPINGS_PATH.write_text(json.dumps(mappings, indent=2))