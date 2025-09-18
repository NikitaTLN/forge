import os

confirm = input("Are you sure you want to create a new repository? (y/n): ").lower() == 'y'
readme = input("Do you want to create a README file? (y/n): ").lower() == 'y'
repo_url = input("Enter the repository url: ")
repo_name = input("Enter the repository name: ")
include_files = input("Do you want to include all the files (git add .)? (y/n) ").lower() == 'y'
path = input("Enter the path where you want to create the repository (default is current directory): ")

def create_repo():
    if path == "":
        return
    else:
        os.system("cd " + path)
    os.system("git init")
    os.system("git branch -M main")
    os.system("git remote add origin " + repo_url)

def create_readme():
    os.system("touch README.md")
    os.system("echo " "# " + repo_name, " >> README.md")
    os.system("git add README.md")

def add_files():
    os.system("git add .")

def push_repo():
    os.system('git commit -m "A: first commit"')
    os.system("git push -u origin main")

if confirm:
    create_repo()
    if readme:
        create_readme()
    if include_files:
        add_files()
    push_repo()
    print("Repository created successfully.")
else:
    print("Operation cancelled.")
