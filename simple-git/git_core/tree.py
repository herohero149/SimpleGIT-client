import struct
import os
from git_core.index import read_index
from git_core.objects import hash_object

def write_tree():
    index = read_index()
    entries = []
    for filename, meta in sorted(index.items()):
        mode = "100644"
        oid = meta["oid"]
        entry = f"{mode} {filename}\0".encode() + bytes.fromhex(oid)
        entries.append(entry)
    tree_content = b"".join(entries)
    tree_sha = hash_object(tree_content, "tree")
    return tree_sha