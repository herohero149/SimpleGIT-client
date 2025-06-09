# 🧵 Simple Git Client — A Minimal Yet Complete Git Implementation in Python

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE) 
[![Build](https://img.shields.io/badge/build-passing-brightgreen)](#) 
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](#) 

---

A fully functional **Git client written in Python**, supporting core operations like:

✨ `init`  
✨ `add`  
✨ `commit`  
✨ `clone`  
✨ `push`  
✨ `pull`  

Built from scratch using **Git’s internal object model**, this tool helps you understand how Git works under the hood — while also being useful for lightweight version control tasks.

---

## 🧰 Features

| Feature         | Status ✅ |
|----------------|-----------|
| Init Repo      | ✅        |
| Add Files      | ✅        |
| Commit Changes | ✅        |
| Clone Remote   | ✅        |
| Push Commits   | ✅        |
| Pull Updates   | ✅        |
| Conflict Merge | ✅        |
| Index Handling | ✅        |
| Object Store   | ✅        |
| Auth Support   | ✅        |
| Config Manager | ✅        |
| Unit Tests     | ✅        |

---

## 📦 Project Structure
simple-git/
├── cli/
│ └── main.py # CLI interface
├── git_core/
│ ├── repo.py # Repository initialization
│ ├── index.py # Staging area management
│ ├── objects.py # Git object store (blob, tree, commit)
│ ├── commit.py # Commit creation logic
│ ├── tree.py # Tree object builder
│ ├── network.py # Smart HTTP Git wire protocol
│ └── utils.py # Utility functions
├── auth/
│ └── credentials.py # Handles username/password input
├── config/
│ └── config.py # .git/config reader/writer
├── tests/
│ └── test_all.py # Unit tests using unittest
├── README.md
└── requirements.txt


---

## 🔧 Installation

### 1. Clone the repo

```bash
git clone https://github.com/ArchieTUX/SimpleGIT-client.git
cd

2. Set up virtual environment
python3 -m venv venv
source venv/bin/activate
