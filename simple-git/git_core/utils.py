# git_core/utils.py

import os
import hashlib
from pathlib import Path

GIT_DIR = ".git"
OBJECTS_DIR = os.path.join(GIT_DIR, "objects")
INDEX_PATH = os.path.join(GIT_DIR, "index")
HEAD_PATH = os.path.join(GIT_DIR, "HEAD")

def get_git_dir():
    if not os.path.exists(GIT_DIR):
        raise Exception("Not a git repository")
    return GIT_DIR

def resolve_object_path(oid):
    return os.path.join(OBJECTS_DIR, oid[:2], oid[2:])

def read_file(path):
    with open(path, "rb") as f:
        return f.read()

def write_file(path, data):
    with open(path, "wb") as f:
        f.write(data)

def parse_git_object(data):
    header, content = data.split(b"\x00", 1)
    obj_type, size = header.decode().split()
    assert int(size) == len(content), "Size mismatch"
    return obj_type, content

def oid_from_hex(hex_oid):
    if len(hex_oid) != 40:
        raise ValueError("Invalid object ID")
    return hex_oid