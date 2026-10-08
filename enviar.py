import requests

try:
    with open("publicados.txt", "r") as f:
        publicados = f.read().splitlines()
except:
    publicados = []

r = requests.get(
    "https://www.amazon.es/gp/goldbox",
    headers={
        "User-Agent": "Mozilla/5.0"
    }
)

print("STATUS:", r.status_code)
print(r.text[:500])
