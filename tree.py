__author__ = "8408206,Ghiaszade Naeini"

def ist_baum(graph):
    start = "a"
    # Starten wir mit dem ersten Knoten
    visited = set()
    parent = {start: None}
    # Wurzel hat kein Elternteil
    hat_zyklus = False

    def dfs(node):
        nonlocal hat_zyklus
        # Weil hat_zyklus außerhalb der Funktion definiert ist,
        # wollen wir es innerhalb der Funktion ändern können
        visited.add(node)

        for nachbar in graph[node]:
            if nachbar not in visited:
                parent[nachbar] = node
                dfs(nachbar)  # rekursiver Aufruf
            elif parent[node] != nachbar:
                hat_zyklus = True

        # Base Case: wenn alle Nachbarn in visited sind, passiert nichts weiter

    # DFS starten
    dfs(start)

    # Zyklus prüfen
    if hat_zyklus:
        print("Der Graph enthält mindestens einen Zyklus. Daher ist er kein Baum.\n")
        return

    # Zusammenhängend?
    if len(visited) != len(graph):
        unerreicht = set(graph.keys()) - visited
        print(f"Der Graph ist nicht zusammenhängend. "
              f"Unerreichbare Knoten: {list(unerreicht)}.\n")
        return

    print("Der Graph ist ein Baum.\n")
