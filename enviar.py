import requests
import re

r = requests.get(
    "https://www.amazon.es/gp/goldbox",
    headers={"User-Agent": "Mozilla/5.0"}
)

print("STATUS:", r.status_code)

# Buscar bloques donde aparece dealID
deals = re.findall(r'"dealID":"([^"]+)"', r.text)

print("DEALS:", len(deals))
print(deals[:10])

# Buscar títulos más legibles
titulos = re.findall(r'"title":"([^"]+)"', r.text)

print("TITULOS:", len(titulos))
print(titulos[:10])
