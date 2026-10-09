import requests
import re
import os
import json

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

# Leer ASIN publicados
try:
    with open("publicados.txt", "r") as f:
        publicados = [line.strip() for line in f if line.strip()]
except:
    publicados = []

print("PUBLICADOS:")
print(publicados)

# Leer Amazon Goldbox
r = requests.get(
    "https://www.amazon.es/gp/goldbox",
    headers={"User-Agent": "Mozilla/5.0"}
)

texto = r.text

# Extraer ASIN, título, link e imagen
productos = re.findall(
    r'"asin":"([^"]+)".*?"title":"([^"]+)".*?"link":"([^"]+)".*?"baseUrl":"([^"]+)"',
    texto,
    re.DOTALL
)

print("PRODUCTOS ENCONTRADOS:", len(productos))

for asin, titulo, link, imagen in productos:

    print("COMPROBANDO:", asin)

    if asin in publicados:
        print("YA PUBLICADO:", asin)
        continue

    print("PUBLICANDO:", asin)

    url = f"https://www.amazon.es{link}?tag=verross-21"

    boton = {
        "inline_keyboard": [[
            {
                "text": "🛒 Comprar en Amazon",
                "url": url
            }
        ]]
    }

    respuesta = requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendPhoto",
        data={
            "chat_id": CHAT_ID,
            "photo": imagen,
            "caption": f"🎁 OFERTA AMAZON 🎁\n\n{titulo}",
            "reply_markup": json.dumps(boton)
        }
    )

    print(respuesta.text)

    with open("publicados.txt", "a") as f:
        f.write(asin + "\n")

    print("GUARDADO:", asin)

    break


