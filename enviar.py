import requests
import re

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

print("PRODUCTOS:", len(productos))

for asin, titulo, link in productos[:10]:
    print("--------")
    print("ASIN:", asin)
    print("TITULO:", titulo)
    print("LINK:", link)

