import os

def set_directory() -> str | None:
    while True:
        name = input("Select output directory: ").strip().strip('"')
        if not name:
            print("Directory name cannot be empty.")
            continue
        if os.path.isdir(name):
            return name
        print(f"Directory does not exist: {name}")