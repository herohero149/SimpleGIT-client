import os
import pickle
from git_core.objects import hash_object

INDEX_PATH = ".git/index"

def read_index():
    if not os.path.exists(INDEX_PATH):
        return {}
    with open(INDEX_PATH, "rb") as f:
        return pickle.load(f)

def write_index(index):
    with open(INDEX_PATH, "wb") as f:
        pickle.dump(index, f)

def add_files(files):
    index = read_index()
    for file in files:
        if os.path.isfile(file):
            with open(file, "rb") as f:
                content = f.read()
            oid = hash_object(content, "blob")
            index[file] = {"oid": oid}
    write_index(index)
    print(f"Added {len(files)} file(s) to index.")