# memory/session_memory.py

import json
import os

MEMORY_FILE = "memory/session.json"


def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return {
            "founder_name": "",
            "startup_idea": "",
            "target_market": "",
            "business_model": "",
            "key_strengths": [],
            "known_gaps": [],
            "refinement_progress": "",
            "conversation_stage": "discovery",
            "evaluation_ready": False

        }

    with open(MEMORY_FILE, "r") as f:
        return json.load(f)


def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)