import requests
import re

r = requests.get(
    "https://www.amazon.es/gp/goldbox",
    headers={"User-Agent": "Mozilla/5.0"}
)

texto = r.text

for palabra in [
    "price",
    "dealPrice",
    "discount",
    "savings",
    "percentage",
    "listPrice",
    "basisPrice",
    "salePrice"
\]:
    print(palabra, "=>", texto.lower().count(palabra.lower()))

