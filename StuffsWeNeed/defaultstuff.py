import json
from dotenv import load_dotenv
import os

def config(filename: str = "config"):
    try:
        with open(f"StuffsWeNeed/jsons/{filename}.json", encoding='utf8') as data:
            return json.load(data)
    except FileNotFoundError:
        raise FileNotFoundError("config.json wasn't found")


def profile(filename: str = "profile"):
    try:
        with open(f"StuffsWeNeed/jsons/{filename}.json", encoding='utf8') as data:
            return json.load(data)
    except FileNotFoundError:
        raise FileNotFoundError("profile.json wasn't found")


def texts(filename: str = "texts"):
    try:
        with open(f"StuffsWeNeed/jsons/{filename}.json", encoding='utf8') as data:
            return json.load(data)
    except FileNotFoundError:
        raise FileNotFoundError("texts.json wasn't found")