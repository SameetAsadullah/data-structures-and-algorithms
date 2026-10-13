# Data Structures and Algorithms in C++

A curated C++ collection spanning linear containers, search trees, graph representations, traversal, and shortest-path algorithms.

The collection keeps the implementation code close to its original design while removing generated build artifacts and presenting a consistent structure across modules.

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
applications/  Applied uses of the implemented structures
graphs/        Graph representations and algorithms
linear/        Sequential and linked containers
trees/         Search trees and balanced trees
```

Each directory retains its implementation-specific README and source layout. Generated executables, compiler output, and IDE caches are excluded.

## Building an implementation

Each implementation can be compiled with a C++17 compiler from its `src` directory:

```bash
c++ -std=c++17 main.cpp -o program
./program
```

The automated repository check performs syntax compilation for every `main.cpp`. Warnings from the original implementations are reported without rewriting their design.

## Provenance and licensing

See [PROVENANCE.md](PROVENANCE.md) for the source mapping. The original repositories did not declare licenses, so this consolidated collection does not broaden reuse permissions.
