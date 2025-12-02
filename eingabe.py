__author__ = "8408206,Ghiaszade Naeini"

import math

koordinaten_database = {}
# Die Namen von Knoten mit x, y-Koordinaten speichern.
graph = {}
# Die Namen von Knoten und deren Nachbarn speichern.
gerichtet = False

def get_eingabe():
    global gerichtet
    # global damit wir es in Funktion erreichen können
    buchstaben = "abcdefghijklmnopqrstuvwxyz"
    ob_gerichtet=input("gerichtet ? (ja oder nein)\n")

    if ob_gerichtet=="ja":
        gerichtet=True
    elif ob_gerichtet=="nein":
        gerichtet=False
    else:
        print("falshe Eingabe\n")
        get_eingabe()

    print("a) die Anzahl von Knoten")
    print("b) die Namen von Knoten")
    print("c) die Koordinaten von Knoten")
    abc1 = input("choose\n")

    match abc1:
        case "a":
            # Verteilen wir alle Knoten auf einem Kreis
            r = 200  # Radius
            anzahl1 = int(input("Wie viele Knoten?\n"))
            for i in range(anzahl1):
                angle_deg = (360 / anzahl1) * i
                angle_rad = math.radians(angle_deg)
                # Damit die Knoten mit gleichen Abständen auf dem Kreis liegen
                x = math.cos(angle_rad) * r
                y = math.sin(angle_rad) * r
                koordinaten_database[buchstaben[i]] = [x, y]

        case "b":
            r = 200
            nodes = input(
                "Give the names of the nodes as a list (e.g : a b c d ...)\n"
            ).split()
            # .split() gibt uns eine Liste von Knoten
            for i in range(len(nodes)):
                angle_deg = (360 / len(nodes)) * i
                angle_rad = math.radians(angle_deg)
                x = math.cos(angle_rad) * r
                y = math.sin(angle_rad) * r
                koordinaten_database[nodes[i]] = [x, y]

        case "c":
            anzahl2 = int(input("Wie viele Knoten würdest du eingeben?\n"))
            for i in range(anzahl2):
                raw = input("Gib die Koordinaten so x,y ein\n")
                # Benutzer gibt z.B.: 200,300
                a, b = raw.split(",")
                # a="200", b="300"
                x, y = int(a), int(b)
                koordinaten_database[buchstaben[i]] = [x, y]

        case _:
            print("Falsche Eingabe\n")
            return

    for node in koordinaten_database:
        verbindungen = input(f"Verbindungen von {node}\n").split()
        graph[node] = verbindungen
    """
    Egal wie wir die Knoten bekommen haben, müssen wir jetzt nach Verbindungen fragen.
    Mit einem for-loop fragen wir das für jeden Knoten und speichern sie in 'graph'.
    'graph' wird später in tree.py, bfs.py ... genutzt.
    """

    return abc1
# Warum machen wir ein return für abc1? Damit wir es in main.py bekommen können!
