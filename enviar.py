import requests

r = requests.get(
    "https://www.amazon.es/gp/goldbox",
    headers={"User-Agent": "Mozilla/5.0"}
)

texto = r.text

asin = "B0F9L3BQ9J"

pos = texto.find(f'"asin":"{asin}"')

print(texto[pos:pos+12000])
