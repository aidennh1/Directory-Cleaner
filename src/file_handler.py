from pathlib import Path
import shutil
import os

def get_file_types(dir_in_str: str) -> set[str]:
    """Return the set of unique file extensions (lowercased) in the given directory.
    
    Files without an extension are represented as the string '(no extension)'.
    Only top-level files are considered; subdirectories are ignored.
    """
    return {
        file.suffix.lower() or "(no extension)"
        for file in Path(dir_in_str).iterdir()
        if file.is_file()
    }

def create_type_folders(directory: str, type_set: set):
    """Create one subdirectory per file extension inside `directory`.
    
    Folder names are the bare extension without a leading dot (e.g. 'pdf', 'txt').
    Files with no extension get a folder named 'no extension'.
    Silently continues if a folder already exists, printing a notice to stdout.
    """
    for ext in type_set:
        ext_str = str(ext).strip('.')   # drop leading dot, e.g. '.pdf' -> 'pdf'
        folder = os.path.join(directory, ext_str)
        try:
            os.mkdir(folder)
        except FileExistsError:
            print(f"Folder '{ext_str}' already exists")

def sort_by_type(dir_in_str: str):
    """Move every file in `dir_in_str` into the matching extension subdirectory.
    
    Calls get_file_types and create_type_folders to ensure destination folders
    exist before moving. Each file is moved atomically via shutil.move.
    """
    directory = Path(dir_in_str)
    type_set = get_file_types(dir_in_str)
    create_type_folders(dir_in_str, type_set)

    for file in directory.iterdir():
        if file.is_file():
            # Derive folder name the same way create_type_folders does
            ext_str = file.suffix.lower().strip('.') or "no extension"
            dest = directory / ext_str / file.name
            shutil.move(str(file), dest)