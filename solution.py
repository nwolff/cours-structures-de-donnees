from operator import attrgetter

from lib import Capitale, distance

capitales = [
    Capitale(nom="Tirana", latitude=41.33, longitude=19.82),
    Capitale(nom="Vienna", latitude=48.21, longitude=16.37),
    Capitale(nom="Minsk", latitude=53.9, longitude=27.57),
    Capitale(nom="Brussels", latitude=50.85, longitude=4.35),
    Capitale(nom="Sarajevo", latitude=43.85, longitude=18.36),
    Capitale(nom="Sofia", latitude=42.7, longitude=23.32),
    Capitale(nom="Zagreb", latitude=45.81, longitude=15.98),
    Capitale(nom="Nicosia", latitude=35.17, longitude=33.37),
    Capitale(nom="Prague", latitude=50.09, longitude=14.42),
    Capitale(nom="Copenhagen", latitude=55.68, longitude=12.57),
    Capitale(nom="Tallinn", latitude=59.44, longitude=24.75),
    Capitale(nom="Tórshavn", latitude=62.01, longitude=-6.77),
    Capitale(nom="Helsinki", latitude=60.17, longitude=24.94),
    Capitale(nom="Paris", latitude=48.85, longitude=2.35),
    Capitale(nom="Berlin", latitude=52.52, longitude=13.41),
    Capitale(nom="Gibraltar", latitude=36.14, longitude=-5.35),
    Capitale(nom="Athens", latitude=37.98, longitude=23.72),
    Capitale(nom="St Peter Port", latitude=49.46, longitude=-2.54),
    Capitale(nom="Budapest", latitude=47.5, longitude=19.04),
    Capitale(nom="Reykjavík", latitude=64.14, longitude=-21.9),
    Capitale(nom="Dublin", latitude=53.33, longitude=-6.25),
    Capitale(nom="Douglas", latitude=54.15, longitude=-4.48),
    Capitale(nom="Rome", latitude=41.89, longitude=12.48),
    Capitale(nom="Saint Helier", latitude=49.19, longitude=-2.1),
    Capitale(nom="Pristina", latitude=42.67, longitude=21.17),
    Capitale(nom="Riga", latitude=56.95, longitude=24.11),
    Capitale(nom="Vilnius", latitude=54.69, longitude=25.28),
    Capitale(nom="Luxembourg", latitude=49.61, longitude=6.13),
    Capitale(nom="Skopje", latitude=42, longitude=21.43),
    Capitale(nom="Chişinău", latitude=47.01, longitude=28.86),
    Capitale(nom="Podgorica", latitude=42.44, longitude=19.26),
    Capitale(nom="Amsterdam", latitude=52.37, longitude=4.89),
    Capitale(nom="Oslo", latitude=59.91, longitude=10.75),
    Capitale(nom="Warsaw", latitude=52.23, longitude=21.01),
    Capitale(nom="Lisbon", latitude=38.72, longitude=-9.13),
    Capitale(nom="Bucharest", latitude=44.43, longitude=26.11),
    Capitale(nom="Moscow", latitude=55.75, longitude=37.62),
    Capitale(nom="Belgrade", latitude=44.8, longitude=20.47),
    Capitale(nom="Bratislava", latitude=48.15, longitude=17.11),
    Capitale(nom="Ljubljana", latitude=46.05, longitude=14.51),
    Capitale(nom="Madrid", latitude=40.42, longitude=-3.7),
    Capitale(nom="Longyearbyen", latitude=78.22, longitude=15.64),
    Capitale(nom="Stockholm", latitude=59.33, longitude=18.06),
    Capitale(nom="Kiev", latitude=50.45, longitude=30.52),
    Capitale(nom="London", latitude=51.51, longitude=-0.13),
    Capitale(nom="Vaduz", latitude=47.14, longitude=9.52),
]

berne = Capitale(nom="Berne", latitude=46.95, longitude=7.45)

# Trouver berne dans la liste

for i in range(len(capitales)):
    capitale = capitales[i]
    if capitale.nom == "Berne":
        berne = capitale

# Afficher la distance entre Berne et chacune des autres capitales
print("Distance de Berne (en km)")
print("-------------------------")
for i in range(len(capitales)):
    capitale = capitales[i]
    distance_de_berne = distance(berne, capitale)
    # distance_de_berne_arrondie = int(distance_de_berne)
    distance_de_berne_arrondie = distance_de_berne
    print(capitale.nom, ":", distance_de_berne_arrondie)


# Afficher la capitale la plus proche de Berne, ainsi que sa distance de berne
plus_petite_distance = 1000000000000
index_de_la_capitale_la_plus_proche = 0
for i in range(len(capitales)):
    capitale = capitales[i]
    distance_de_berne = distance(berne, capitale)
    if distance_de_berne < plus_petite_distance:
        plus_petite_distance = distance_de_berne
        index_de_la_capitale_la_plus_proche = i

print("Capitale la plus proche: ")
print(capitales[index_de_la_capitale_la_plus_proche])

# Afficher dans l'ordre les 5 capitales les plus proches de Berne,
# y compris leur distance à berne

# Avec sort
for i in range(0, len(capitales)):
    capitale = capitales[i]
    distance_de_berne_arrondie = int(distance(berne, capitale))
    capitale.distance = distance_de_berne_arrondie

capitale_ordonnèes = sorted(capitales, key=attrgetter("distance"))
for i in range(10):
    capitale = capitale_ordonnèes[i]
    print(capitale.nom, capitale.distance)
