__author__ = "8408206,Ghiaszade Naeini"

from collections import deque


def shortest_path(graph, start, goal):
    queue = deque([[start]])
    visited = set([start])
    # Weil wir repetitive Knoten nicht wollen

    while queue:
        # Solange queue nicht leer ist
        path = queue.popleft()
        # Entfernung von links (FIFO)
        node = path[-1]
        """
        Das letzte Element von path.
        Warum? 
        Weil wir new_path in queue hinzufügen. new_path hat mehrere Elemente,
        aber wir wollen nur das letzte. Also entfernen wir es mit popleft() von queue
        und holen es mit [-1].
        """

        if node == goal:
            print(path)
            return

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                new_path = path + [neighbor]
                # Path aktualisieren
                queue.append(new_path)

    print(f"Es gibt keinen Weg zwischen {start} und {goal}\n")
    # Falls kein Weg gefunden wurde