import requests
import base64
import os
from auth.credentials import get_credentials
from git_core.repo import init_repo

def clone_repo(url, path):
    print(f"Cloning into {path}...")
    url = url.rstrip("/")
    git_url = url + "/info/refs?service=git-upload-pack"
    headers = {
        "Accept": "application/x-git-upload-pack-advertisement"
    }
    auth = get_credentials()
    if auth:
        headers["Authorization"] = f"Basic {auth}"
    response = requests.get(git_url, headers=headers)
    if response.status_code != 200:
        raise Exception("Failed to fetch refs")
    os.makedirs(path, exist_ok=True)
    os.chdir(path)
    init_repo()
    print("Repo cloned.")

def push_to_remote(remote="origin", branch="main"):
    print(f"Pushing to {remote}/{branch}")
    # Implement smart HTTP upload pack here

def fetch_from_remote(remote="origin", branch="main"):
    print(f"Fetching from {remote}/{branch}")
    # Implement fetch logic