# Graph — Visualization and Graph Algorithms

A Python project for creating, visualizing, and analyzing graphs. It provides an interactive command-line interface for configuring a graph, drawing it with Turtle Graphics, checking whether it is a tree, and finding a shortest path between two vertices.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [How It Works](#how-it-works)
- [Requirements](#requirements)
- [Installation](#installation)
- [Run the Program](#run-the-program)
- [Using the Program](#using-the-program)
- [Project Structure](#project-structure)
- [Algorithms](#algorithms)
- [Current Limitations](#current-limitations)

## Overview

This project demonstrates fundamental graph concepts and algorithms in Python. Users can define vertices and their connections, choose whether the graph is directed or undirected, and then select an operation from a text-based menu.

The project combines graph input, visualization, graph traversal, shortest-path search, and tree checking in a small modular application.

## Features

### Flexible graph setup

The program offers three ways to define the vertices and their positions:

1. **Choose the number of vertices.** The program names the vertices with lowercase letters and places them around a circle.
2. **Choose vertex names.** The user enters custom vertex names, which are arranged around a circle.
3. **Enter coordinates.** The user provides an x-coordinate and y-coordinate for each vertex, allowing more control over the layout.

After defining the vertices, the user enters the neighbors connected to each vertex.

### Directed and undirected graphs

During setup, the user can choose a directed or undirected graph.

- **Directed graph:** edges are displayed with arrowheads to indicate direction.
- **Undirected graph:** connections are drawn without arrowheads.

For an undirected graph, enter the connections consistently in both directions so that the graph representation matches the intended undirected edges.

### Graph visualization

The project uses Python's built-in `turtle` module to draw the graph.

- Vertices are displayed as colored circles.
- Vertex names are written beside or over their circles.
- Edges are drawn between the configured vertices.
- Directed edges include arrowheads.
- Custom coordinates let users control the placement of vertices.

Vertex colors are selected randomly from a predefined list, so the colors may differ between runs.

### Shortest-path search

The program uses **Breadth-First Search (BFS)** to find a shortest path between a start vertex and a target vertex in an unweighted graph. If no path is found, it prints a message indicating that the vertices are not connected by a path.

### Tree checking

The program includes a tree-checking operation based on **Depth-First Search (DFS)**. It checks for cycles and whether all vertices are reachable from the starting vertex.

## How It Works

At a high level, the application follows this workflow:

1. Choose how to define the vertices and their positions.
2. Choose whether the graph is directed or undirected.
3. Enter the neighbors for each vertex.
4. Select an operation:
   - Draw the graph.
   - Check whether the graph is a tree.
   - Find the shortest path between two vertices.

## Requirements

- Python 3
- The standard-library `turtle` module
- A graphical desktop environment capable of opening a Turtle window

The source code currently uses Python's `match` statement, so **Python 3.10 or newer** is recommended.

No third-party Python packages are required by the source files included in this project.

## Installation

Clone the repository:

```bash
git clone https://github.com/bardiaghiaszade/Graph.git
cd Graph
```

Check your Python version:

```bash
python --version
```

If your system uses `python3`, use:

```bash
python3 --version
```

## Run the Program

From the project directory, run:

```bash
python main.py
```

Or, on systems where the command is `python3`:

```bash
python3 main.py
```

The program will first ask you to configure the graph, then display the operation menu.

## Using the Program

### Step 1: Choose the graph direction

When prompted, enter:

- `ja` for a directed graph.
- `nein` for an undirected graph.

These options are currently expected in German, as shown in the program prompts.

### Step 2: Choose how to define the vertices

Enter one of the following menu options:

- `a` — Enter the number of vertices. The program arranges them around a circle and names them with lowercase letters.
- `b` — Enter custom vertex names separated by spaces. The program arranges them around a circle.
- `c` — Enter the number of vertices and then provide each vertex's coordinates in `x,y` format.

For example, a coordinate can be entered as:

```text
200,100
```

### Step 3: Define connections

For every vertex, enter the names of its neighboring vertices separated by spaces, following the prompt displayed by the program.

Make sure that every referenced vertex exists. For an undirected graph, represent each connection consistently from both endpoints.

### Step 4: Select an operation

The main menu provides these options:

| Input | Operation | Description |
|---|---|---|
| `a` | Draw graph | Opens a Turtle window and draws the vertices and edges. |
| `b` | Is the graph a tree? | Checks for cycles and connectivity using DFS. |
| `c` | Shortest path | Asks for a start and target vertex and searches with BFS. |

For the shortest-path option, enter the start vertex when prompted with `von:` and the target vertex when prompted with `bis:`.

## Project Structure

| File | Responsibility |
|---|---|
| `main.py` | Starts the program, displays the menu, and calls the selected operation. |
| `eingabe.py` | Collects graph settings, vertex names, coordinates, and connections. |
| `zeichnen.py` | Draws vertices and edges using Turtle Graphics. |
| `bfs.py` | Implements breadth-first search for shortest-path finding. |
| `tree.py` | Checks graph connectivity and cycles to determine whether the graph is a tree. |
| `.gitignore` | Lists generated and local files that Git should ignore. |

## Algorithms

### Breadth-First Search (BFS)

BFS explores a graph level by level, starting from a selected vertex. In an unweighted graph, this finds a path containing the minimum number of edges, provided a path exists.

For a standard adjacency-list implementation, BFS has a time complexity of **O(V + E)** and a space complexity of **O(V)**, where `V` is the number of vertices and `E` is the number of edges. The current implementation stores complete paths in its queue, so its practical memory usage can differ from a conventional parent-pointer BFS implementation.

### Depth-First Search (DFS) for tree checking

The tree-checking function uses recursive DFS to visit vertices, detect cycles, and compare the number of visited vertices with the total number of vertices.

A tree is a connected, acyclic, undirected graph. The current implementation starts its traversal at the vertex named `a`, so the graph must contain that vertex for the check to work as intended. The graph's connections should also be represented consistently as an undirected graph for the result to match the standard mathematical definition of a tree.