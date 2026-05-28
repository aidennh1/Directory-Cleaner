from pathlib import Path
import shutil
import os

def get_file_types(dir_in_str: str) -> set[str]:
    return {
        file.suffix.lower() or "(no extension)"
        for file in Path(dir_in_str).iterdir()
        if file.is_file()
    }

def create_type_folders(directory: str, type_set: set):
    for ext in type_set:
        ext_str = str(ext).strip('.')
        folder = os.path.join(directory, ext_str)
        try:
            os.mkdir(folder)
        except FileExistsError:
            print(f"Folder '{ext_str}' already exists")

def sort_by_type(dir_in_str: str):
    directory = Path(dir_in_str)
    type_set = get_file_types(dir_in_str)
    create_type_folders(dir_in_str, type_set)

    for file in directory.iterdir():
        if file.is_file():
            ext_str = file.suffix.lower().strip('.') or "no extension"
            dest = directory / ext_str / file.name
            shutil.move(str(file), dest)