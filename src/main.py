import parser
import file_handler

def main():
    # Prompt for a valid directory, then sort its contents by file type
    dir_path = parser.set_directory()
    file_handler.sort_by_type(dir_path)

if __name__ == '__main__':
    main()