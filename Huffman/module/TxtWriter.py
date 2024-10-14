class TxtWriter:
    @staticmethod
    def code_writer(coded_string_to_code, output_file):
        with open(output_file, 'wb') as file:
            file.write(coded_string_to_code)  

    @staticmethod
    def write_file(decoded_string, output_file):
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(decoded_string)
