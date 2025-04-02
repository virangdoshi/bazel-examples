import requests

r = requests.get("http://localhost:8081", timeout=60)
print(r.json())
