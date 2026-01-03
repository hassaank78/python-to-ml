import json

data = {
    "user": "Alice",
    "active": True,
    "scores": [85, 92, 78]
}

with open('response.json', 'w') as f:
    json.dump(data, f, indent=2)

with open('response.json', 'r') as f:
    data = json.load(f)
    print(data["scores"])