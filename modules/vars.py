import os

API_ID    = os.environ.get("API_ID", "22694914")
API_HASH  = os.environ.get("API_HASH", "4fd02c02368941a03d48ecab3a3b4a31")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
