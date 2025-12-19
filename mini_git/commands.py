from . import objects
from . import index
from . import refs

import os
import json

def cmd_init():
    objects.init_storage()
    index.init_index()
    refs.init_refs()
    print("Initialized empty mini git repo")

def cmd_add(filename):
    if not os.path.exists(filename):
        print(f"error: file not found: {filename}")
        return
    
    with open(filename, "rb") as f:
        data = f.read()

    blob_oid = objects.write_blob(data)
    idx = index.load_index()
    idx[filename] = blob_oid
    index.save_index(idx)

    print(f"added {filename}")

def cmd_commit(message):
    idx = index.load_index()
    if not idx:
        print("Nothing to commit")
        return
    
    tree_data = json.dumps(idx, sort_keys=True).encode()
    tree_oid = objects.write_tree(tree_data)

    parent = refs.get_head()

    commit_data = {
        "tree" : tree_oid,
        "parent" : parent,
        "message" : message
    }
    commit_oid = objects.write_commit(json.dumps(commit_data).encode())
    refs.set_head(commit_oid)

    print(f"Committed as {commit_oid}")

def cmd_log():
    oid = refs.get_head()
    if not oid:
        print("no commits yet")
        return

    while oid:
        commit_raw = objects.read_object(oid)
        commit = json.loads(commit_raw.decode())

        print(f"commit {oid}")
        print(f"    {commit['message']}")
        print()

        oid = commit.get("parent", "")