import requests
import re
import json

r = requests.get(
    "https://www.amazon.es/gp/goldbox",
    headers={"User-Agent": "Mozilla/5.0"}
)

texto = r.text

inicio = texto.find('"products":[')

if inicio == -1:
    print("No encontrado")
    exit()

print("ENCONTRADO")

print(texto[inicio:inicio+5000])
