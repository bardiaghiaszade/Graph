import Knoten
import turtle
import Kanten


def main():   
    gerichtet=False

    print("a)die anzahl von knoten")
    print("b)die Namen von knoten")
    print("c)die koordinaten von knoten")
    eingabe=input("choose\n")

    t = turtle.Turtle()
    t.hideturtle()
    t.penup()


    match eingabe:

        case "a":
            Knoten.self_nodes(t)
            
        case "b":
            Knoten.user_nodes(t)

        case "c":
            Knoten.koordinaten_knoten(t)
        case _:
            print("ridi")
    
    Kanten.draw_kanten(t)
    turtle.done()
if __name__ == "__main__":
    main()