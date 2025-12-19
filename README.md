# Mini‑git (Python)

This project is a small re‑implementation of Git’s core ideas, originally inspired by a Java assignment and rewritten in Python to relearn the fundamentals. It focuses on the essential building blocks of a version‑control system: object storage, hashing, the index, commits, and history traversal. The implementation is intentionally minimal to strengthen Python skills while leaving room for future experimentation.

---

## Features

- Initialize a repository (`init`)
- Add files to the index (`add`)
- Create commits (`commit`)
- View commit history (`log`)
- SHA‑1 object storage (blobs, trees, commits)
- Simple refs system (`HEAD`)
- Human‑readable object format (JSON)

---

## Repository Structure
mini-git-project/
│
├── mini_git/
│   ├── init.py
│   ├── main.py
│   ├── commands.py
│   ├── objects.py
│   ├── index.py
│   └── refs.py
│
├── a.txt
└── README.md


When initialized, the project creates a `.minigit/` directory:
.minigit/
├── objects/  # stored blobs, trees, commits
├── index/    # staging area
└── HEAD      # current commit reference

---

## Usage

Run commands using:
    python -m mini_git <command> [args]

### Initialize a repository
    python -m mini_git init\

### Add a file to the index
    python -m mini_git add <filename>

### Commit staged changes
    python -m mini_git commit "message"

### View commit history
    python -m mini_git log
