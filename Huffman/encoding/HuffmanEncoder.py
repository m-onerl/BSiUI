import math
import os
from module.TxtReader import TxtReader
from module.TxtWriter import TxtWriter

class HuffmanEncoder:
    def __init__(self):
        self.string_to_code = ""
        self.sorted_unique_char = ""
        self.file_name = ""
        self.bit_string = ""
        self.letter_to_binary_map = {}
        self.num_bits = 0

    def encode_string(self, output_file="examples/codedExample.txt"):
 
        self.encode_dictionary()

        characters_in_set = len(self.sorted_unique_char)
        print(f"Characters in set (during encoding): {characters_in_set}")
        
     
        for char in self.string_to_code:
            self.bit_string += self.letter_to_binary_map[char]

   
        padding_length = (8 - len(self.bit_string) % 8) % 8
        padding = '0' * padding_length
        self.bit_string += padding

        binary_data = bytearray()
        for i in range(0, len(self.bit_string), 8):
            byte = self.bit_string[i:i + 8]
            binary_data.append(int(byte, 2))  

 
        with open(output_file, 'wb') as file:
            file.write(bytes([characters_in_set])) 
            for char in self.sorted_unique_char:
                file.write(char.encode('utf-8')) 
            file.write(binary_data)  

    def encode_dictionary(self):

        self.file_read(os.path.join("examples", self.file_name))
        self.sort_unique_characters(self.string_to_code)

        num_unique_chars = len(self.sorted_unique_char)
        self.num_bits = math.ceil(math.log2(num_unique_chars))
        print(f"Liczba bitów potrzebna na znak: {self.num_bits}")


        for i, char in enumerate(self.sorted_unique_char):
            binary_code = format(i, f'0{self.num_bits}b')
            self.letter_to_binary_map[char] = binary_code
            print(f"Character: {char}, Code: {binary_code}")

    def sort_unique_characters(self, string_to_code):
        unique_chars = sorted(set(string_to_code))
        self.sorted_unique_char = "".join(unique_chars)

    def file_read(self, file_name):
        self.string_to_code = TxtReader.read_file(file_name)
