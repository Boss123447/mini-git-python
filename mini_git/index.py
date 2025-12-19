import os
import json

ROOT = ".minigit"
INDEX_PATH = os.path.join(ROOT, "index")

def init_index():
    os.makedirs(ROOT, exist_ok=True)
    if not os.path.exists(INDEX_PATH):
        with open(INDEX_PATH, "w") as f:
            json.dump({}, f)

def load_index() -> dict:
    if not os.path.exists(INDEX_PATH):
        return {}
    with open(INDEX_PATH, "r") as f:
        return json.load(f)
    
def save_index(idx: dict):
    with open(INDEX_PATH, "w") as f:
        json.dump(idx, f, indent=2)