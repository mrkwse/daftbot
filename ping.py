import requests

something = {"a": "1", "b": "2"}

requests.post("http://127.0.0.1:5000/", params=something)
requests.post("http://127.0.0.1:5000/PS4/", params=something)
requests.post("http://127.0.0.1:5000/PC/", params=something)
