__author__ = "8408206,Ghiaszade Naeini"

import eingabe
import zeichnen
import turtle
import bfs
import tree


def main():
    abc1 = eingabe.get_eingabe()
    # abc1 gibt an, wie der Benutzer die Knoten eingeben möchte

    print("a) Graph zeichnen")
    print("b) Ist Baum?")
    print("c) Kürzeste Pfad zwischen 2 Knoten")
    abc2 = input("choose\n")
    # abc2 gibt an, welche Aktion der Benutzer ausführen möchte

    if abc2 == "a":
        zeichnen.draw_knoten()
        zeichnen.draw_kanten()
        turtle.done()
        """
        turtle.done() ist hier geschrieben und nicht in zeichnen.py.
        Warum? Wenn es in zeichnen.py wäre, würde durch import ein Screen geöffnet werden,
        bevor wir überhaupt etwas eingeben.
        """
    elif abc2 == "b":
        tree.ist_baum(eingabe.graph)
    elif abc2 == "c":
        start = input("von:\n")
        goal = input("bis:\n")
        bfs.shortest_path(eingabe.graph, start, goal)
    else:
        print("falsche Eingabe\n")
        return


if __name__ == "__main__":
    main()
