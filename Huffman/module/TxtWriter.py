class TxtWriter:
    @staticmethod
    def code_writer(coded_string_to_code, coded_string, output_file):

        with open(output_file, 'wb') as file:
            file.write(coded_string)
            one_char = ""
            binary_data = bytearray()
            for i in range(0, len(coded_string_to_code), 8):
                one_char = coded_string_to_code[i:i + 8]
                int_value = int(one_char, 2)
                binary_data.append(int_value)
            file.write(bytes(binary_data))

    @staticmethod
    def write_file(decoded_string, output_file):
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(decoded_string)