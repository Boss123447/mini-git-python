import os
import hashlib
import json

ROOT = ".minigit"
OBJ_DIR = os.path.join(ROOT, 'objects')

def init_storage():
    os.makedirs(OBJ_DIR, exist_ok=True)

def sha1(data: bytes) -> str:
    return hashlib.sha1(data).hexdigest()
    
def write_object(data: bytes) -> str:
    oid = sha1(data)
    path = os.path.join(OBJ_DIR, oid)
    with open(path, "wb") as f:
        f.write(data)
    return oid

def read_object(oid: str) -> bytes:
    path = os.path.join(OBJ_DIR, oid)
    with open(path, "rb") as f:
        return f.read()
    
def write_blob(data: bytes) -> str:
    return write_object(data)

def write_tree(data: bytes) -> str:
    return write_object(data)

def write_commit(data: bytes) -> str:
    return write_object(data)