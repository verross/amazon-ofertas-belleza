import requests
import re
import os
import json

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

r = requests.get(
    "https://www.amazon.es/gp/goldbox",
    headers={"User-Agent": "Mozilla/5.0"}
)

texto = r.text

productos = re.findall(
    r'"asin":"([^"]+)".*?"title":"([^"]+)".*?"link":"([^"]+)"',
    texto,
    re.DOTALL
)

asin, titulo, link = productos[0]

url = f"https://www.amazon.es{link}?tag=verross-21"
