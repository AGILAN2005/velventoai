import json
from pathlib import Path

DB_PATH = Path("db/users.json")

def load_users():
    if not DB_PATH.exists():
        DB_PATH.write_text("{}")
    return json.loads(DB_PATH.read_text())

def save_users(data):
    DB_PATH.write_text(json.dumps(data, indent=2))

def get_user(username):
    users = load_users()
    return users.get(username)

def register_user(username, topic):
    users = load_users()
    users[username] = {
        "topic": topic,
        "irt_score": 0.5,
        "history": []
    }
    save_users(users)

def update_user(username, user_data):
    users = load_users()
    users[username] = user_data
    save_users(users)
