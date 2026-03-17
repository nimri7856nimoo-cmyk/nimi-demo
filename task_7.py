import requests
import json

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)

data = response.json()

selected = [{"id": item["id"], "title": item["title"]} for item in data]

with open("output.json", "w") as f:
    json.dump(selected, f, indent=4)

print("Data saved to output.json")