import parser
import file_handler

def main():
    dir_path = parser.set_directory()
    file_handler.create_type_folder(dir_path, file_handler.get_file_types(dir_path))
if __name__ == '__main__':
    main()