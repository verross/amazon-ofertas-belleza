import requests

url = "https://www.amazon.es/gp/goldbox"

r = requests.get(
    url,
    headers={
        "User-Agent": "Mozilla/5.0"
    }
)

print("STATUS:", r.status_code)
print(r.text[:1000])
