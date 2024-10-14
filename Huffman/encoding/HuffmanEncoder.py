from module.TxtReader import TxtReader
from module.TxtWriter import TxtWriter
import os 

class HuffmanEncoder:
    def __init__(self):
        self.string_to_code = ""
        self.sorted_unique_char = ""
        self.file_name = ""
        self.coded_string = ""
        self.coded_string_to_code = ""
        self.binary_modulo = ""
        self.modulo = 0
        self.letter_to_binary_map = {}

    def encode_string(self, output_file="examples/codedExample.txt"):
        self.encode_dictionary()

        characters_in_set = len(self.sorted_unique_char)
        print(f"Characters in set (during encoding): {characters_in_set}")
        
        self.coded_string = bytes([characters_in_set])
        
        self.coded_string += self.sorted_unique_char.encode('utf-8')

        for char in self.string_to_code:
            self.coded_string_to_code += self.letter_to_binary_map[char]


        padding_length = (8 - len(self.coded_string_to_code) % 8) % 8
        padding = '0' * padding_length 
        self.coded_string_to_code += padding

        padding_info = format(padding_length, '03b')
        self.coded_string_to_code = padding_info + self.coded_string_to_code

  
        TxtWriter.code_writer(self.coded_string_to_code, self.coded_string, output_file)

    def encode_dictionary(self):
        self.file_read(os.path.join("examples", self.file_name))
        self.sort_unique_characters(self.string_to_code)

        binary = "00"
        for char in self.sorted_unique_char:
            self.letter_to_binary_map[char] = binary
            print(f"Character: {char}, Code: {binary}")  
            binary = self.increment_binary(binary)

    def increment_binary(self, binary):
        value = int(binary, 2)
        value += 1
        return format(value, '02b')

    def sort_unique_characters(self, string_to_code):
        unique_chars = sorted(set(string_to_code))
        self.sorted_unique_char = "".join(unique_chars)

    def file_read(self, file_name):
        self.string_to_code = TxtReader.read_file(file_name)
