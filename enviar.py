import requests
import re

r = requests.get(
    "https://www.amazon.es/gp/goldbox",
    headers={"User-Agent": "Mozilla/5.0"}
)

texto = r.text

patron = r'"priceToPay".*?"price":"([^"]+)".*?"basisPrice".*?"price":"([^"]+)".*?"text":"([^"]+%)"'

ofertas = re.findall(patron, texto, re.DOTALL)

print("OFERTAS:", len(ofertas))

for actual, anterior, descuento in ofertas[:10]:
    print("------")
    print("ANTES:", anterior)
    print("AHORA:", actual)
    print("DTO:", descuento)

