import requests

r = requests.get(
    "https://www.amazon.es/gp/goldbox",
    headers={"User-Agent": "Mozilla/5.0"}
)

texto = r.text

pos = texto.find('"priceToPay"')

print(texto[pos-2000:pos+3000])
