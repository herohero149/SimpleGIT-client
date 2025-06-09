import os
import hashlib
import zlib

def hash_object(data, obj_type):
    header = f"{obj_type} {len(data)}\0".encode()
    full_data = header + data
    sha = hashlib.sha1(full_data).hexdigest()
    path = os.path.join(".git", "objects", sha[:2], sha[2:])
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if not os.path.exists(path):
        with open(path, "wb") as f:
            f.write(zlib.compress(full_data))
    return sha