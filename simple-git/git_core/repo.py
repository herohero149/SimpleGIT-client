import os

GIT_DIR = ".git"

def init_repo(path="."):
    os.makedirs(os.path.join(path, GIT_DIR), exist_ok=True)
    os.makedirs(os.path.join(path, GIT_DIR, "objects"), exist_ok=True)
    os.makedirs(os.path.join(path, GIT_DIR, "refs", "heads"), exist_ok=True)
    print(f"Initialized empty Git repo in {os.path.abspath(GIT_DIR)}")