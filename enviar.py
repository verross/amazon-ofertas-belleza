import requests
import re
import os
import json

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

# Leer publicados
try:
    with open("publicados.txt", "r") as f:
        publicados = [line.strip() for line in f if line.strip()]
except:
    publicados = []

# Descargar Goldbox
r = requests.get(
    "https://www.amazon.es/gp/goldbox",
    headers={"User-Agent": "Mozilla/5.0"}
)

texto = r.text

# Buscar productos
productos = re.findall(
    r'"asin":"([^"]+)"'
    r'.*?"title":"([^"]+)"'
    r'.*?"link":"([^"]+)"'
    r'.*?"baseUrl":"([^"]+)"',
    texto,
    re.DOTALL
)

print("PRODUCTOS:", len(productos))

for asin, titulo, link, imagen in productos:

    if asin in publicados:
        continue

    inicio = texto.find(f'"asin":"{asin}"')

    bloque = texto[inicio:inicio+6000]

    precio_actual = re.search(
        r'"priceToPay".*?"price":"([^"]+)"',
        bloque,
        re.DOTALL
    )

    precio_anterior = re.search(
        r'"basisPrice".*?"price":"([^"]+)"',
        bloque,
        re.DOTALL
    )

    descuento = re.search(
        r'"text":"([0-9]+%)"',
        bloque,
        re.DOTALL
    )

    if not precio_actual:
        continue

    actual = precio_actual.group(1)

    anterior = (
        precio_anterior.group(1)
        if precio_anterior
        else "-"
    )

    dto = (
        descuento.group(1)
        if descuento
        else "-"
    )

    imagen = imagen.replace("\\/", "/")

    if not imagen.endswith(".jpg"):
        imagen += ".jpg"

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
        f"💰 Antes: {anterior} €\n"
        f"🔥 Ahora: {actual} €\n"
        f"🏷️ Descuento: {dto}"
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
