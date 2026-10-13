import requests
import re
import os
import json
from datetime import datetime

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

BELLEZA = [
    "crema",
    "serum",
    "sérum",
    "perfume",
    "cosmética",
    "champú",
    "champu",
    "facial",
    "piel",
    "maquillaje",
    "oneblade",
    "philips",
    "afeitado"
]

MASCOTAS = [
    "perro",
    "perros",
    "gato",
    "gatos",
    "mascota",
    "mascotas",
    "pienso",
    "comida para perros",
    "comida para gatos",
    "rascador",
    "arenero",
    "correa",
    "arnés",
    "arnes",
    "juguete para perros",
    "juguete para gatos",
    "cama para perro",
    "cama para gato",
    "transportín",
    "transportin",
    "comedero",
    "bebedero",
    "purina",
    "royal canin",
    "advance",
    "ultima",
    "whiskas",
    "felix",
    "pedigree"
]

HOGAR = [
    "aspirador",
    "robot",
    "cafetera",
    "freidora",
    "escritorio",
    "mesa",
    "limpieza",
    "hogar",
    "mueble",
    "vela",
    "colchón",
    "colchon",
    "almohada"
]

TECNO = [
    "iphone",
    "samsung",
    "xiaomi",
    "redmi",
    "poco",
    "realme",
    "motorola",
    "oneplus",
    "pixel",
    "portátil",
    "portatil",
    "laptop",
    "tablet",
    "ipad",
    "auriculares",
    "smartwatch",
    "bluetooth",
    "gaming",
    "ordenador",
    "echo",
    "alexa",
    "ring",
    "kindle",
    "fire tv"
]

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

# Extraer productos
productos = re.findall(
    r'"asin":"([^"]+)"'
    r'.*?"title":"([^"]+)"'
    r'.*?"link":"([^"]+)"'
    r'.*?"baseUrl":"([^"]+)"',
    texto,
    re.DOTALL
)

print("PRODUCTOS:", len(productos))

ahora = datetime.utcnow()

for asin, titulo, link, imagen in productos:

    if asin in publicados:
        continue

    titulo_lower = titulo.lower()

    categoria = None

    if any(x in titulo_lower for x in BELLEZA):
        categoria = "💄 BELLEZA"

    elif any(x in titulo_lower for x in MASCOTAS):
        categoria = "🐶 MASCOTAS"

    elif any(x in titulo_lower for x in HOGAR):
        categoria = "🏠 HOGAR"

    elif any(x in titulo_lower for x in TECNO):
        categoria = "📱 TECNOLOGÍA"

    else:
        continue
        

    print("CATEGORIA:", categoria)
    print("MINUTO:", ahora.minute)    
    if categoria == "💄 BELLEZA":
    print("BELLEZA")
    if ahora.minute % 8 != 0:
        print("NO TOCA")
        continue
    # Frecuencias

    if categoria == "💄 BELLEZA":
        if ahora.minute % 8 != 0:
            continue

    elif categoria == "🐶 MASCOTAS":
        if ahora.minute % 8 != 0:
            continue

    elif categoria == "🏠 HOGAR":
        if ahora.minute % 20 != 0:
            continue

    elif categoria == "📱 TECNOLOGÍA":
        if ahora.minute % 20 != 0:
            continue

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
        f"{categoria}\n\n"
        f"📦 {titulo}"
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
