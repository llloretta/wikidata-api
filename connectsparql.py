import requests

params = {
        "language": "en",
        "format" : "json"}

# url = "https://www.wikidata.org/wiki/Special:EntityData/Q3004.json"
# data = requests.get(url,params=params)
# print(data.json())

data = requests.get('https://www.wikidata.org/wiki/Special:EntityData/Q544944.json', params=params)
print("get object to relation P31", data.json()["entities"]["Q544944"]["claims"]["P31"][0]["mainsnak"]["datavalue"]["value"]["id"])

