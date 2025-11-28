import random
import math

farben = ["blue", "green", "purple", "orange", "red", "pink", "cyan"]
buchstaben = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
koordinaten_database = {}



def self_nodes(t):
    
    anzahl = int(input("gib die Anzahl\n"))
    r = 200

    for i in range(anzahl):
        angle_deg = (360 / anzahl) * i
        angle_rad = math.radians(angle_deg)

        x = math.cos(angle_rad) * r
        y = math.sin(angle_rad) * r

        t.goto(x, y)
        t.dot(40, random.choice(farben))
        t.goto(x + 2, y - 8)
        t.write(buchstaben[i], align="center", font=("Arial", 12, "bold"))

        koordinaten_database[buchstaben[i]] = [x, y]


def user_nodes(t):
    nodes = input("Give the names of the nodes as a list (e.g : A B C D ...)\n").split()

    anzahl = len(nodes)
    r = 200

    for i in range(anzahl):
        angle_deg = (360 / anzahl) * i
        angle_rad = math.radians(angle_deg)

        x = math.cos(angle_rad) * r
        y = math.sin(angle_rad) * r

        t.goto(x, y)
        t.dot(40, random.choice(farben))
        t.goto(x + 2, y - 8)
        t.write(nodes[i], align="center", font=("Arial", 12, "bold"))

        koordinaten_database[nodes[i]] = [x, y]
    
    
def koordinaten_knoten(t):
    
    anzahl = int(input("Wie viele Knoten würest du eingeben?\n"))
    
    for i in range(anzahl):
        raw = input("Gib die Koordinaten so x,y ein\n")
        a, b = raw.split(",")
        x, y = int(a), int(b)
        koordinaten_database[buchstaben[i]] = [x, y]

    for k, v in koordinaten_database.items():
        x=(v[0])
        y=(v[1])
        
        t.goto(x,y)
        t.dot(40, random.choice(farben))
        t.goto(x + 2, y - 8)
        t.write(k, align="center", font=("Arial", 12, "bold"))