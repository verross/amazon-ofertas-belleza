import requests

r = requests.get(
    "https://www.amazon.es/gp/goldbox",
    headers={"User-Agent": "Mozilla/5.0"}
)

texto = r.text

pos = texto.find('"asin":"B0DTQCWJBR"')

print(texto[pos:pos+6000])
