__author__ = "8408206,Ghiaszade Naeini"

import turtle
import random
import eingabe

def setup_turtle():
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    return t


farben = ["blue", "green", "purple", "orange", "red", "pink", "cyan"]

kd = eingabe.koordinaten_database
gph = eingabe.graph

def draw_knoten():
    t = setup_turtle()
    for key, (x, y) in kd.items():
        t.goto(x, y)
        t.dot(40, random.choice(farben))
        t.goto(x + 2, y - 8)
        t.write(key, align="center", font=("Arial", 12, "bold"))

        """
        Jedes Mal geht Turtle zu den Koordinaten eines Knotens
        (diese Koordinaten kommen aus unserem koordinaten_database in eingabe.py)
        und zeichnet einen Punkt dort. Dieser Punkt hat eine zufällige Farbe und Größe 40.
        Warum dann t.goto(x + 2, y - 8)?
        Damit der Name in der Mitte des Punktes steht.
        Danach wird der Name mit t.write(key, align="center", font=("Arial", 12, "bold")) geschrieben.
        """


def draw_kanten():
    t = setup_turtle()
    for key, val in gph.items():
        x, y = kd[key]
        t.penup()
        t.goto(x, y)
        """
        Erstmal nimmt Turtle key (Name des Knotens) aus gph
        und kontrolliert, welche Koordinaten er in kd hat.
        Dann ohne zu zeichnen (penup()) geht er zu diesen Koordinaten.
        """
        for i in range(len(val)):
            t.pendown()
            x2, y2 = kd[val[i]]
            if eingabe.gerichtet:
                # Pfeilspitze berechnen (2/3 des Weges)
                x3= x + (x2 - x) * (2/3)
                y3= y + (y2 - y) * (2/3)

                t.goto(x3,y3)

                # Pfeil zeichnen
                angel = t.towards(x2,y2)
                t.setheading(angel)
                t.shape("arrow")
                t.shapesize(1,1)
                t.stamp()
                t.hideturtle()
            """
            wenn es gerichtet ist dann bild einen Pfeil damit die
            Richtung gezeichnet wird
            """

            t.goto(x2, y2)
            t.goto(x, y)
            """
            Mit diesem for-loop ist Turtle auf einem Knoten.
            Jetzt kontrolliert der Loop, welche Nachbarn dieser Knoten hat.
            Für jeden Nachbarn werden die Koordinaten aus kd geholt,
            Turtle geht zu diesem Nachbarn und kommt zurück,
            damit er zum nächsten Nachbarn gehen kann.
            """
 