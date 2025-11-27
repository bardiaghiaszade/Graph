import turtle
import random
import math


koordinaten=[]
buchstaben="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
anzahl=int(input("gib die Anzahl\n"))
farben = ["blue", "green", "purple", "orange", "red", "pink", "cyan"]
t = turtle.Turtle()
t.penup()
"""for i in range(anzahl):
    x=random.randint(-400,400)
    y=random.randint(-400,400)
    koordinaten.append((x,y))



t.goto(koordinaten[-1][0],koordinaten[-1][1])
t.dot(100,random.choice(farben))
t.pendown()
"""
"""for i in range(len(koordinaten)-1):
    t.goto(koordinaten[i][0],koordinaten[i][1])
   """
r = 200
for i in range(1,anzahl+1):
    angle = (360//anzahl ) * i *4
    x = math.cos(angle) * r
    y = math.sin(angle) * r
    t.goto(x, y)
    t.dot(40,random.choice(farben))

turtle.done()

