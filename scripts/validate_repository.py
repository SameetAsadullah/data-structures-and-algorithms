#!/usr/bin/env python3
"""Validate repository structure and syntax-check each C++ implementation."""

from __future__ import annotations

import shutil
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
IMPLEMENTATIONS = (
    "linear/array-list",
    "linear/singly-linked-list",
    "linear/doubly-linked-list",
    "linear/circular-linked-list",
    "linear/stack",
    "linear/queue",
    "linear/vector",
    "trees/binary-search-tree",
    "trees/avl-tree",
    "graphs/graph",
    "graphs/dijkstra",
    "applications/bracket-validation",
)
GENERATED_DIRECTORIES = {".vs", "Debug", "Release", "ipch", "x64", "x86"}
GENERATED_SUFFIXES = {
    ".aps", ".exe", ".ilk", ".obj", ".pdb", ".sdf", ".suo", ".tlog", ".user"
}


def tracked_files() -> list[Path]:
    output = subprocess.check_output(["git", "ls-files"], cwd=ROOT, text=True)
    return [ROOT / line for line in output.splitlines()]


def validate_layout(errors: list[str]) -> None:
    for relative in IMPLEMENTATIONS:
        directory = ROOT / relative
        if not (directory / "README.md").is_file():
            errors.append(f"missing README: {relative}")
        if not (directory / "src" / "main.cpp").is_file():
            errors.append(f"missing entry point: {relative}/src/main.cpp")


def validate_generated_files(errors: list[str]) -> None:
    for path in tracked_files():
        if GENERATED_DIRECTORIES.intersection(path.parts) or path.suffix.lower() in GENERATED_SUFFIXES:
            errors.append(f"generated artifact is tracked: {path.relative_to(ROOT)}")


def validate_cpp(errors: list[str]) -> None:
    compiler = shutil.which("c++")
    if not compiler:
        errors.append("no C++ compiler found")
        return

    for relative in IMPLEMENTATIONS:
        source = ROOT / relative / "src" / "main.cpp"
        result = subprocess.run(
            [compiler, "-std=c++17", "-fsyntax-only", str(source)],
            cwd=source.parent,
            text=True,
            capture_output=True,
        )
        if result.returncode:
            errors.append(f"syntax check failed: {source.relative_to(ROOT)}\n{result.stderr}")


def main() -> int:
    errors: list[str] = []
    validate_layout(errors)
    validate_generated_files(errors)
    validate_cpp(errors)

    if errors:
        print("Repository validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Validated {len(IMPLEMENTATIONS)} C++ implementations.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
