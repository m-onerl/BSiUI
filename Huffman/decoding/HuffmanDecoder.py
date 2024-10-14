import math
from module.TxtReader import TxtReader
from module.TxtWriter import TxtWriter

class HuffmanDecoder:
    def __init__(self):
        self.coded_string = b""
        self.binary_chars = ""
        self.decoded_string = ""
        self.codes = {}
        self.num_bits = 0

    def decoder(self, input_file="examples/codedExample.txt", output_file="examples/zdekompresowany.txt"):
        self.coded_file_reader(input_file)
        if len(self.coded_string) == 0:
            print("Error: coded_string is empty.")
            return
        characters_in_set = self.coded_string[0]
        print(f"Characters in set (during decoding): {characters_in_set}")


        self.num_bits = math.ceil(math.log2(characters_in_set))
        offset = 1 + characters_in_set 
        for i in range(characters_in_set):
            char = chr(self.coded_string[i + 1])
            binary_code = format(i, f'0{self.num_bits}b')
            self.codes[binary_code] = char
        print(f"Decoded dictionary: {self.codes}")
        
        encoded_data = self.coded_string[offset:]
        self.binary_chars = ''.join(format(byte, '08b') for byte in encoded_data)


        decoded_output = []
        buffer = ""
        for bit in self.binary_chars:
            buffer += bit
            if buffer in self.codes:
                decoded_output.append(self.codes[buffer])
                buffer = ""

        self.decoded_string = "".join(decoded_output)
        TxtWriter.write_file(self.decoded_string, output_file)
        print(f"Plik został odkodowany i zapisany w {output_file}.")

    def coded_file_reader(self, input_file):
        with open(input_file, 'rb') as f:
            self.coded_string = f.read()
