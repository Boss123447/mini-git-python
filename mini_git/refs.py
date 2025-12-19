import os

ROOT = ".minigit"
HEAD_PATH = os.path.join(ROOT, "HEAD")


def init_refs():
    os.makedirs(ROOT, exist_ok=True)
    if not os.path.exists(HEAD_PATH):
        with open(HEAD_PATH, "w") as f:
            f.write("")


def get_head() -> str:
    if not os.path.exists(HEAD_PATH):
        return ""
    with open(HEAD_PATH, "r") as f:
        return f.read().strip()


def set_head(oid: str):
    with open(HEAD_PATH, "w") as f:
        f.write(oid)