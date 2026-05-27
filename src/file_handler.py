from pathlib import Path

def get_file_types(dir_in_str: str) -> set[str]:
    return {
        file.suffix.lower() or "(no extension)"
        for file in Path(dir_in_str).iterdir()
        if file.is_file()
    }