# forge 🔨

Forge is a simple Python script that bootstraps a new Git repository with minimal setup.  
It helps you initialize a project, create a README file, and push everything to a remote repository with just a few prompts.

---

# ✨ Features
- Initialize a new Git repository
- Optionally create a `README.md` with the project name
- Add all files or just the README
- Configure remote origin
- Make the first commit and push to `main`

---

# 🛠️ Requirements
- Python 3.x
- Git installed and configured on your machine
- Internet connection for pushing to remote repository
- (Optional) GitHub CLI (`gh`) for creating a remote repository easily

---

# 🚀 Usage
1. Clone or download this project.
```bash
git clone https://github.com/NikitaTLN/forge.git
cd forge
mv forge.py ~/.local/bin/
cd ..
rm -rf forge/
cd ~/.local/bin/
python3 forge.py
```

2. It is recommended to set a keyboard shortcut for running the script quickly.
## Zsh:

```bash
echo "bindkey -s 'YOURKEY' 'python3 ~/.local/bin/forge.py \n'" >> ~/.zshrc
```

### for example:

```bash
echo "bindkey -s '^g' 'python3 ~/.local/bin/forge.py \n'" >> ~/.zshrc
# bind ctrl+g to run dive
```

## Bash:

```bash
echo "bind -x '"YOURKEY":"python3 ~/.local/bin/forge.py"'" >> ~/.bashrc
```

### for example:

```bash
echo "bind -x '"\C-g":"python3 ~/.local/bin/forge.py"'" >> ~/.bashrc
# bind ctrl+g to run dive
```
