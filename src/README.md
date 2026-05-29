# File Sorter

Organizes a flat directory by moving files into subdirectories named after their extension.

```
my_folder/
├── report.pdf      →  my_folder/pdf/report.pdf
├── photo.JPG       →  my_folder/jpg/photo.JPG
├── notes.txt       →  my_folder/txt/notes.txt
└── Makefile        →  my_folder/no extension/Makefile
```

## Usage

```bash
python main.py
```

You'll be prompted to enter a directory path. Paste or type an absolute or relative path; surrounding quotes are stripped automatically.

## Modules

| Module | Purpose |
|---|---|
| `main.py` | Entry point |
| `file_handler.py` | Extension detection, folder creation, and file moving |
| `parser.py` | Interactive directory prompt with input validation |

## Behavior

- Extensions are normalized to lowercase.
- Files with no extension go into a folder named `no extension`.
- If a destination folder already exists, it is reused and a notice is printed.
- Subdirectories inside the target folder are never moved.

## Requirements

Python 3.10+ (uses `X | Y` union type hints). No third-party dependencies.