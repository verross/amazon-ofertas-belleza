import requests

r = requests.get(
    "https://www.amazon.es/gp/goldbox",
    headers={"User-Agent": "Mozilla/5.0"}
)

texto = r.text

pos = texto.find("B0C6F6KKLD")

print(texto[pos:pos+4000])

