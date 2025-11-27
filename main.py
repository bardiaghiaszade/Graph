import Knoten

def main():   
    gerichtet=False

    print("a)die anzahl von knoten")
    print("b)die Namen von knoten")
    print("c)die koordinaten von knoten")
    eingabe=input("choose\n")

    match eingabe:

        case "a":
            Knoten.self_nodes()
    
        case "b":
            Knoten.user_nodes()

        case "c":
            Knoten.koordinaten_knoten()
        case _:
            print("ridi")

if __name__ == "__main__":
    main()