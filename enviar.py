import requests
import re
import json

r = requests.get(
    "https://www.amazon.es/gp/goldbox",
    headers={"User-Agent": "Mozilla/5.0"}
)

texto = r.text

m = re.search(r'"products":\[(.*?)\],"totalCount"', texto)

if not m:
    print("No encontrado")
    exit()

productos = "[" + m.group(1) + "]"

datos = json.loads(productos)

print("PRODUCTOS:", len(datos))

for p in datos[:5\]:
    print("------")
    print("ASIN:", p.get("asin"))
    print("TITULO:", p.get("title"))
    print("LINK:", p.get("link"))
