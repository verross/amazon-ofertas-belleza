import requests
import re

r = requests.get(
    "https://www.amazon.es/gp/goldbox",
    headers={"User-Agent": "Mozilla/5.0"}
)

print("STATUS:", r.status_code)

# Buscar precios
precios = re.findall(r'€', r.text)

print("Simbolos euro encontrados:", len(precios))

# Buscar títulos
titulos = re.findall(r'"title":"([^"]+)"', r.text)

print("Titulos encontrados:", len(titulos))

if titulos:
    print(titulos[:5])
