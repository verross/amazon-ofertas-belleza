import requests
import re
import os
import json

print("PASO 1")

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

print("PASO 2")

r = requests.get(
    "https://www.amazon.es/gp/goldbox",
    headers={"User-Agent": "Mozilla/5.0"}
)

print("PASO 3")

coincidencias = re.findall(r'/dp/([A-Z0-9]{10})', r.text)

print("PASO 4")

print(coincidencias[:5])
