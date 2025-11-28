from Knoten import koordinaten_database, farben


def create_kanten(t):
    graph = {}
    for node in koordinaten_database:
        verbindungen = input(f"Verbindiungen von {node[0]}\n").split()
        graph[node[0]] = verbindungen
    print(graph)
    print(koordinaten_database)
    return graph

def draw_kanten(t):
    graph = create_kanten(t)

    for key, val in graph.items():
        x, y = koordinaten_database[key]
        t.penup()
        t.goto(x, y)
        
        for i in range(len(val)):
            t.pendown()
            x2, y2 = koordinaten_database[val[i]]
            t.goto(x2,y2)
            t.goto(x,y)