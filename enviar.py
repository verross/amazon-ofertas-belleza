import requests
import re
import os
import json
from datetime import datetime, timedelta

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

BELLEZA = [
    # Cosmética general
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
    "afeitado",
    "oneblade",
    "philips",

    # Coreana
    "anua",
    "biodance",
    "celimax",
    "skin1004",
    "beauty of joseon",
    "boj",
    "cosrx",
    "round lab",
    "mixsoon",
    "medicube",
    "dr.althea",
    "dr althea",
    "haruharu",
    "haruharu wonder",
    "numbuzin",
    "isntree",
    "some by mi",
    "somebymi",
    "laneige",
    "etude",
    "etude house",
    "rom&nd",
    "romand",
    "torriden",
    "heimish",
    "iunik",
    "abib",
    "axis-y",
    "axis y",
    "pyunkang yul",
    "dear klairs",
    "klairs",
    "purito",
    "anua",
"biodance",
"celimax",
"skin1004",
"beauty of joseon",
"cosrx",
"round lab",
"mixsoon",
"medicube",
"numbuzin",
"torriden",
"haruharu",
"isntree",


    # Dermocosmética
    "cerave",
    "ceravé",
    "isdin",
    "eucerin",
    "vichy",
    "la roche",
    "la roche-posay",
    "neutrogena",
    "roc",
    "sesderma",
    "avene",
    "avène",
    "bioderma",

    # Marcas populares
    "loreal",
    "l'oréal",
    "garnier",
    "nivea",
    "dove",

    # Palabras frecuentes
    "toner",
    "tónico",
    "tonico",
    "retinol",
    "vitamina c",
    "niacinamida",
    "ácido hialurónico",
    "acido hialuronico",
    "limpiador facial",
    "protector solar",
    "spf",
    "sunscreen",
    "ampoule",
    "essence",
    "mask",
    "sheet mask",
    "mascarilla facial"

]


def puede_publicar(archivo, minutos):
    try:
        with open(archivo, "r") as f:
            contenido = f.read().strip()

        if contenido:
            ultima = datetime.fromisoformat(contenido)

            if datetime.now() - ultima < timedelta(minutes=minutos):
                return False

    except:
        pass

    return True


def guardar_publicacion(archivo):
    with open(archivo, "w") as f:
        f.write(datetime.now().isoformat())


# Leer publicados
try:
    with open("publicados.txt", "r") as f:
        publicados = [line.strip() for line in f if line.strip()]
except:
    publicados = []

# Leer Goldbox
r = requests.get(
#    "https://www.amazon.es/gp/goldbox",
    "https://www.amazon.es/deals?ref_=nav_cs_gb&discounts-widget=%2522%257B%255C%2522state%255C%2522%253A%257B%255C%2522refinementFilters%255C%2522%253A%257B%255C%2522departments%255C%2522%253A%255B%255C%25226198055031%255C%2522%255D%257D%257D%252C%255C%2522version%255C%2522%253A1%257D%2522&promotionsSearchLastSeenAsin=B0GTJ653VG&promotionsSearchStartIndex=0&promotionsSearchPageSize=90",
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/138.0 Safari/537.36",
        "Accept-Language": "es-ES,es;q=0.9"
    }
)

# Leer deals
#r = requests.get(
#    "https://www.amazon.es/deals",
#    headers={"User-Agent": "Mozilla/5.0"}
#)
texto = r.text
asins = re.findall(r'"asin":"([^"]+)"', texto)

print("ASINS ENCONTRADOS:", len(asins))
print("ASINS ÚNICOS:", len(set(asins)))

print("TAMAÑO HTML:", len(texto))



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


print("ASINS ENCONTRADOS:", len(asins))
print("ASINS ÚNICOS:", len(set(asins)))
productos_belleza = []

for asin, titulo, link, imagen in productos:

    if asin in publicados:
        continue

    titulo_lower = titulo.lower()

    print("TITULO:", titulo)

    for palabra in BELLEZA:
        if palabra in titulo_lower:
            print("COINCIDE CON:", palabra)
            productos_belleza.append(
                (asin, titulo, link, imagen, "💄 BELLEZA")
            )
            break

if not productos_belleza:
    print("NO HAY PRODUCTOS DE BELLEZA")
    exit()

producto_seleccionado = None

if productos_belleza and puede_publicar("ultima_belleza.txt", 5):
    producto_seleccionado = productos_belleza[0]

if not producto_seleccionado:
    print("NO HAY PRODUCTOS DE BELLEZA")
    exit()

asin, titulo, link, imagen, categoria = producto_seleccionado

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

    guardar_publicacion("ultima_belleza.txt")

    print("GUARDADO:", asin)
exit()
