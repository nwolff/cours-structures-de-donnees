from collections import namedtuple
from dataclasses import dataclass
from math import atan2, cos, radians, sin, sqrt

Capitale_old = namedtuple("Capitale", ["nom", "latitude", "longitude"])


@dataclass
class Capitale:
    nom: str
    latitude: float
    longitude: float
    distance: float = 0


def distance(p1, p2):
    """
    From https://stackoverflow.com/questions/19412462/getting-distance-between-two-points-based-on-latitude-longitude

    """

    # Rayon approximatif de la terre en km
    R = 6373.0

    lat1 = radians(p1.latitude)
    lon1 = radians(p1.longitude)
    lat2 = radians(p2.latitude)
    lon2 = radians(p2.longitude)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return R * c
