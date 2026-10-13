import requests

r = requests.get(
    "https://www.amazon.es/gp/goldbox",
    headers={"User-Agent": "Mozilla/5.0"}
)

texto = r.text

inicio = texto.find('"productSearchResponse":{"nextIndex"')

print(texto[inicio:inicio+2000])
