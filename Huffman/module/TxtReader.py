class TxtReader:
    @staticmethod
    def read_file(file_name, binary=False):
        try:
            mode = 'rb' if binary else 'r'
            with open(file_name, mode) as file:
                return file.read()
        except FileNotFoundError:
            print(f"File {file_name} not found.")
            return b"" if binary else ""