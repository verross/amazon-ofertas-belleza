import requests
import re

r = requests.get(
    "https://www.amazon.es/gp/goldbox",
    headers={"User-Agent": "Mozilla/5.0"}
)

print("STATUS:", r.status_code)

# Buscar ASINs
asins = re.findall(r'/dp/([A-Z0-9]{10})', r.text)

print("ASINS:", len(asins))
print(asins[:10])

# Buscar URLs de imágenes Amazon
imagenes = re.findall(r'https://m\.media-amazon\.com/images/I/[^"]+', r.text)

print("IMAGENES:", len(imagenes))
print(imagenes[:5])
