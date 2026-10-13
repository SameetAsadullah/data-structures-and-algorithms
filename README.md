# Data Structures and Algorithms in C++

A curated collection of C++ implementations developed while learning core data structures, graph representations, traversal, and shortest-path algorithms.

The implementation code remains close to the original projects. This repository consolidates the work, removes generated Visual Studio artifacts, and provides a single map of the concepts covered.

## Contents

| Category | Implementations |
|---|---|
| Linear structures | [Array list](linear/array-list), [singly linked list](linear/singly-linked-list), [doubly linked list](linear/doubly-linked-list), [circular linked list](linear/circular-linked-list), [stack](linear/stack), [queue](linear/queue), and [vector](linear/vector) |
| Trees | [Binary search tree](trees/binary-search-tree) and [AVL tree](trees/avl-tree) |
| Graphs | [Graph representation and traversal](graphs/graph), and [Dijkstra's shortest path](graphs/dijkstra) |
| Application | [Curly-bracket validation](applications/bracket-validation) using a stack |

## Design focus

- Templated containers where present in the original work
- Manual memory management and pointer-based structures
- Common traversal and mutation operations
- Progressive implementation from linear structures to trees and graphs

## Repository layout

```text
applications/  Small uses of the implemented structures
graphs/        Graph representations and algorithms
linear/        Sequential and linked containers
trees/         Search trees and balanced trees
```

Each directory retains the original project README and source layout. Generated executables, compiler output, and Visual Studio database files are excluded.

## Building an exercise

The original Visual Studio solution and project files are retained. The source can also be compiled with a C++17 compiler from an exercise's `src` directory:

```bash
c++ -std=c++17 main.cpp -o demo
./demo
```

The automated repository check performs syntax compilation for every `main.cpp`. Warnings from the original learning implementations are reported without rewriting their design.

## Provenance and licensing

See [PROVENANCE.md](PROVENANCE.md) for the source mapping. The original repositories did not declare licenses, so this consolidated collection does not broaden reuse permissions.
