import requests
import re
import os
import json

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

# Leer ASIN ya publicados
try:
    with open("publicados.txt", "r") as f:
        publicados = [line.strip() for line in f if line.strip()]
except:
    publicados = []

# Leer Amazon Goldbox
r = requests.get(
    "https://www.amazon.es/gp/goldbox",
    headers={"User-Agent": "Mozilla/5.0"}
)

texto = r.text

# Buscar productos con precio
patron = re.compile(
    r'"asin":"([^"]+)".*?'
    r'"title":"([^"]+)".*?'
    r'"link":"([^"]+)".*?'
    r'"baseUrl":"([^"]+)".*?'
    r'"priceToPay":\{"label":"[^"]*","price":"([^"]+)".*?'
    r'"basisPrice":\{"label":"[^"]*","price":"([^"]+)".*?'
    r'"text":"-?([0-9]+%)"',
    re.DOTALL
)

productos = patron.findall(texto)

print("PRODUCTOS ENCONTRADOS:", len(productos))

for asin, titulo, link, imagen, precio, precio_anterior, descuento in productos:

    if asin in publicados:
        continue

    imagen = imagen.replace("\\/", "/")

    if not imagen.endswith(".jpg"):
        imagen = imagen + ".jpg"

    url = f"https://www.amazon.es{link}?tag=verross-21"

    boton = {
        "inline_keyboard": [[
            {
                "text": "🛒 VER OFERTA",
                "url": url
            }
        ]]
    }

    mensaje = (
        f"🔥 OFERTAZA AMAZON 🔥\n\n"
        f"📦 {titulo}\n\n"
        f"💰 Antes: {precio_anterior} €\n"
        f"🔥 Ahora: {precio} €\n"
        f"🏷️ Descuento: {descuento}"
    )

    respuesta = requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendPhoto",
        data={
            "chat_id": CHAT_ID,
            "photo": imagen,
            "caption": mensaje,
            "reply_markup": json.dumps(boton)
        }
    )

    print(respuesta.text)

    if '"ok":true' in respuesta.text:
        with open("publicados.txt", "a") as f:
            f.write(asin + "\n")

        print("GUARDADO:", asin)

    break
