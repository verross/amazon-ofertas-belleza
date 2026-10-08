import requests

r = requests.get(
    "https://www.amazon.es/gp/goldbox",
    headers={"User-Agent": "Mozilla/5.0"}
)

texto = r.text

pos = texto.find("Amazon Fire TV Stick")

print("POSICION:", pos)

if pos != -1:
    print(texto[pos-500:pos+1500])
