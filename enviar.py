import requests

r = requests.get(
    "https://www.amazon.es/gp/goldbox",
    headers={"User-Agent": "Mozilla/5.0"}
)

texto = r.text

for palabra in [
    "basisPrice",
    "discount",
    "price",
    "percentage"
]:
    pos = texto.find(palabra)

    print("\n====================")
    print("PALABRA:", palabra)
    print("====================")

    if pos != -1:
        print(texto[pos-500:pos+1500])

