from pathlib import Path
import os

def get_file_types(dir_in_str: str) -> set[str]:
    return {
        file.suffix.lower() or "(no extension)"
        for file in Path(dir_in_str).iterdir()
        if file.is_file()
    }

def create_type_folder(type_set: set, directory: str):
    for type in type_set:
        try:
            type_str = str(type).strip('.')
            os.mkdir(f"{directory}\{type_str}")
        except FileExistsError:
            print(f"Folder {type_str} already exists")
