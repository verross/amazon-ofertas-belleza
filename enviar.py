import requests
import re

r = requests.get(
    "https://www.amazon.es/gp/goldbox",
    headers={
        "User-Agent": "Mozilla/5.0"
    }
)

print("STATUS:", r.status_code)

coincidencias = re.findall(r'/dp/([A-Z0-9]{10})', r.text)

print("Productos encontrados:", len(coincidencias))
print(coincidencias[:20])
