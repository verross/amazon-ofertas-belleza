import requests
import re

r = requests.get(
    "https://www.amazon.es/gp/goldbox",
    headers={"User-Agent": "Mozilla/5.0"}
)

coincidencias = re.findall(r'/dp/([A-Z0-9]{10})', r.text)

asin = coincidencias[0]

print("ASIN:", asin)

url = f"https://www.amazon.es/dp/{asin}"

r2 = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"}
)

print("STATUS PRODUCTO:", r2.status_code)

print(r2.text[:1000])
