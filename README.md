# Struct Graph

C++ implementations of linear containers, search trees, graph representations, traversal, and shortest-path algorithms.

The modules use a consistent source layout and automated C++17 syntax checks. Generated build artifacts are excluded from version control.

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
- Operations on linear structures, trees, and graphs

## Repository layout

```text
applications/  Applied uses of the implemented structures
graphs/        Graph representations and algorithms
linear/        Sequential and linked containers
trees/         Search trees and balanced trees
```

Each directory includes implementation-specific usage guidance and source. Generated executables, compiler output, and IDE caches are excluded.

## Building an implementation

Each implementation can be compiled with a C++17 compiler from its `src` directory:

```bash
c++ -std=c++17 main.cpp -o program
./program
```

The automated repository check performs syntax compilation for every `main.cpp`. Compiler warnings are reported without altering runtime behavior.

## Provenance and licensing

See [PROVENANCE.md](PROVENANCE.md) for source history and licensing. No repository-wide open-source license is declared.
