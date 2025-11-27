import turtle
import random
import math

farben = ["blue", "green", "purple", "orange", "red", "pink", "cyan"]
buchstaben = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def self_nodes():
    

    anzahl = int(input("gib die Anzahl\n"))
    r = 200

    t = turtle.Turtle()
    t.hideturtle()
    t.penup()

    for i in range(anzahl):
        angle_deg = (360 / anzahl) * i
        angle_rad = math.radians(angle_deg)

        x = math.cos(angle_rad) * r
        y = math.sin(angle_rad) * r

        t.goto(x, y)
        t.dot(40, random.choice(farben))
        t.goto(x + 2, y - 8)
        t.write(buchstaben[i], align="center", font=("Arial", 12, "bold"))

    turtle.done()


def user_nodes():
    nodes = input("Give the names of the nodes as a list (e.g : A B C D ...)\n").split()

    
    
    anzahl = len(nodes)
    r = 200

    t = turtle.Turtle()
    t.hideturtle()
    t.penup()

    for i in range(anzahl):
        angle_deg = (360 / anzahl) * i
        angle_rad = math.radians(angle_deg)

        x = math.cos(angle_rad) * r
        y = math.sin(angle_rad) * r

        t.goto(x, y)
        t.dot(40, random.choice(farben))
        t.goto(x + 2, y - 8)
        t.write(nodes[i], align="center", font=("Arial", 12, "bold"))
    turtle.done()
    
def koordinaten_knoten():
    koordinaten = []
    anzahl = int(input("Wie viele Knoten würest du eingeben?\n"))
    
    for i in range(anzahl):
        raw = input("Gib die Koordinaten so x,y ein\n")
        a, b = raw.split(",")
        koordinaten.append((int(a),int(b)))
   

    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    

    for i in range(len(koordinaten)):
        x=(koordinaten[i][0])
        y=(koordinaten[i][1])
        
        t.goto(x,y)
        t.dot(40, random.choice(farben))
        t.goto(x + 2, y - 8)
        t.write(buchstaben[i], align="center", font=("Arial", 12, "bold"))
    turtle.done()
