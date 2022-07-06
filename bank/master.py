import json
with open("countries.json") as f:
    data =json.load(f)

print(len(data))