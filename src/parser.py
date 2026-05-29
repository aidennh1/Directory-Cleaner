import os

def set_directory() -> str | None:
    """Prompt the user for an existing directory path and return it.
    
    Strips surrounding whitespace and quotes from the input (handles paths
    drag-dropped into a terminal on Windows/macOS). Loops until the user
    provides a path that exists and is a directory.
    """
    while True:
        name = input("Select output directory: ").strip().strip('"')
        if not name:
            print("Directory name cannot be empty.")
            continue
        if os.path.isdir(name):
            return name
        print(f"Directory does not exist: {name}")