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

MASCOTAS = [
    "gato",
    "gatos",
    "mascota",
    "mascotas",
    "pienso",
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
    # Pienso y alimentación gatos
"royal canin",
"purina",
"purina one",
"purina pro plan",
"ultima",
"whiskas",
"felix",
"advance",
"hills",
"hill's",
"true instinct",
"applaws",
"nature's variety",
"acana",
"orijen",
"ownat",
"josera",
"carnilove",
"edgard cooper",
"schesir",
"animonda",
"cat chow",
"gourmet",
"gourmet gold",
"sheba",
"lily's kitchen",
"concept for life",
"lifelong",
"arquivet",
"brit care",
"fokker",
"taste of the wild",

# Palabras frecuentes
"arena para gatos",
"arena aglomerante",
"rascador",
"árbol para gatos",
"arbol para gatos",
"fuente para gatos",
"comedero automático",
"comedero automatico",
"bebedero para gatos",
"snack para gatos",
"premio para gatos",
"malta para gatos",
"hierba gatera",
"catnip"
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

    # Control de frecuencia por categoría
    if categoria == "💄 BELLEZA":
        if not puede_publicar("ultima_belleza.txt", 5):
            continue

    elif categoria == "🐶 MASCOTAS":
        if not puede_publicar("ultima_mascotas.txt", 8):
            continue

    elif categoria == "🏠 HOGAR":
        if not puede_publicar("ultima_hogar.txt", 45):
            continue

    elif categoria == "📱 TECNOLOGÍA":
        if not puede_publicar("ultima_tecno.txt", 60):
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

        if categoria == "💄 BELLEZA":
            guardar_publicacion("ultima_belleza.txt")

        elif categoria == "🐶 MASCOTAS":
            guardar_publicacion("ultima_mascotas.txt")

        elif categoria == "🏠 HOGAR":
            guardar_publicacion("ultima_hogar.txt")

        elif categoria == "📱 TECNOLOGÍA":
            guardar_publicacion("ultima_tecno.txt")

        print("GUARDADO:", asin)

    break
