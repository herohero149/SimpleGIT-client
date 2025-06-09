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

## 🛠️ Setup Instructions

### 1. Clone this repo:

```bash
git clone https://github.com/ArchieTUX/SimpleGIT-client.git
cd SimpleGIT-client
```

### 2. Set up a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🚀 Usage Guide

### 🧱 Initialize a new repo:

```bash
python cli/main.py init
```

### 📥 Clone a remote repo:

```bash
python cli/main.py clone https://github.com/example/repo.git 
```

### ➕ Stage files:

```bash
echo "Hello World" > hello.txt
python cli/main.py add hello.txt
```

### 📦 Commit changes:

```bash
python cli/main.py commit -m "Initial commit"
```

### 🚀 Push to remote:

```bash
python cli/main.py push --remote origin --branch main
```

### 🔄 Pull from remote:

```bash
python cli/main.py pull --remote origin --branch main
```

---

## 🧪 Run Tests

Run all tests using `pytest`:

```bash
python -m pytest tests/
```

### ✅ Coverage:

```bash
coverage run -m pytest tests/
coverage report -m
```

---

## 🛠️ Dev Tools

### ✨ Format code:

```bash
black git_core/ cli/ config/ auth/
```

### 🚨 Lint:

```bash
flake8 git_core/ cli/ config/ auth/
```

### 🧠 Type check:

```bash
mypy git_core/ cli/ config/ auth/
```

---

## 🤝 Contributing

Pull requests are welcomed like long-lost friends 🫱🏼‍🫲🏽

1. Fork the repo
2. Create a new branch
3. Make your changes
4. Submit a PR!

---

## 📄 License

MIT Licensed. Check out `LICENSE` for details.

---

## 💬 Questions?

Open an issue or hit me up via GitHub.
Let’s build a better Git, one commit at a time.

---

## ⭐ Show Some Love

If you dig it, star it ⭐
If you break it, patch it 🩹
If you improve it, PR it 🚀

Git reimagined. Minimal. Powerful. Yours.

👉 [SimpleGIT-client GitHub Repo](https://github.com/ArchieTUX/SimpleGIT-client)

