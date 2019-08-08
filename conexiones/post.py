import requests
r = requests.post("http://127.0.0.1:8000/registro/", data={'id': '15 99 6f e2', 'lector': 'lector03'})
print(r.status_code, r.reason)