# config/config.py

import configparser
import os

GIT_DIR = ".git"
CONFIG_PATH = os.path.join(GIT_DIR, "config")

def load_config():
    config = configparser.ConfigParser()
    if os.path.exists(CONFIG_PATH):
        config.read(CONFIG_PATH)
    return config

def save_config(config):
    with open(CONFIG_PATH, "w") as f:
        config.write(f)

def set_remote(name, url):
    config = load_config()
    section = f"remote \"{name}\""
    if not config.has_section(section):
        config.add_section(section)
    config.set(section, "url", url)
    config.set(section, "fetch", "+refs/heads/*:refs/remotes/origin/*")
    save_config(config)
    print(f"Added remote {name}")

def get_remote_url(name="origin"):
    config = load_config()
    section = f"remote \"{name}\""
    if not config.has_section(section):
        raise Exception(f"Remote {name} not found")
    return config.get(section, "url")