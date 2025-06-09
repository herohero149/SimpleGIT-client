import time
import os
from git_core.tree import write_tree
from git_core.objects import hash_object

def create_commit(message):
    tree_sha = write_tree()
    parent = None
    head_path = ".git/HEAD"
    if os.path.exists(head_path):
        with open(head_path, "r") as f:
            ref = f.read().strip()
        if ref.startswith("ref: "):
            ref_path = ref[5:]
            if os.path.exists(".git/" + ref_path):
                with open(".git/" + ref_path) as f:
                    parent = f.read().strip()
    author = "User <user@example.com>"
    timestamp = int(time.time())
    tz = "+0000"
    commit_data = (
        f"tree {tree_sha}\n"
        f"parent {parent}\n" if parent else ""
        f"author {author} {timestamp} {tz}\n"
        f"committer {author} {timestamp} {tz}\n\n"
        f"{message}\n"
    ).encode()
    commit_sha = hash_object(commit_data, "commit")
    print(f"[master (root-commit) {commit_sha[:7]}] {message}")
    with open(".git/refs/heads/main", "w") as f:
        f.write(commit_sha)
    with open(".git/HEAD", "w") as f:
        f.write("ref: refs/heads/main")
    return commit_sha