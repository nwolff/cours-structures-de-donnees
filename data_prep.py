import json
from lib import Capitale


def to_capital_object(data):
    properties = data["properties"]
    lon, lat = data["geometry"]["coordinates"]
    return Capitale(nom=properties["capital"], latitude=lat, longitude=lon)


with open("data/europe-capitals.json") as f:
    j = json.load(f)
    capitals = [to_capital_object(o) for o in j]
    print(repr(capitals))
